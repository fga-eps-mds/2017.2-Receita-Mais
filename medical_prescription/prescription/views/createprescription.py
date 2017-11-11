# Django
from django.views.generic import FormView
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.forms import formset_factory
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django
from user.decorators import is_health_professional
from prescription.forms import (CreatePrescriptionForm,
                                MedicinePrescriptionForm,
                                RecommendationPrescriptionForm,
                                ExamPrescriptionForm,
                                )
from prescription.models import (PrescriptionHasManipulatedMedicine,
                                 PrescriptionHasMedicine,
                                 PrescriptionRecommendation,
                                 PrescriptionDefaultExam,
                                 PrescriptionCustomExam,
                                 PatientPrescription,
                                 NoPatientPrescription
                                 )
from exam.models import CustomExam
from disease.models import Disease
from user.models import (Patient,
                         HealthProfessional,
                         )


class CreatePrescriptionView(FormView):
    """
    Responsible for rendering to fields.
    """
    template_name = 'show_prescription_medicine.html'
    # Defines that these forms will have multiple instances.
    MedicinePrescriptionFormSet = formset_factory(MedicinePrescriptionForm)
    RecommendationPrescriptionFormSet = formset_factory(RecommendationPrescriptionForm)
    ExamPrescriptionFormSet = formset_factory(ExamPrescriptionForm)

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(CreatePrescriptionView, self).dispatch(*args, **kwargs)

    def create_prescription(self, form, request):
        """
        Creates the prescription object.
        """
        patient = form.cleaned_data.get('patient')
        patient_id = form.cleaned_data.get('patient_id')
        cid_id = form.cleaned_data.get('cid_id')

        if cid_id is not None:
            disease = Disease.objects.get(pk=cid_id)
        else:
            disease = None

        if patient_id is None or patient_id is 0:
            prescription_object = self.create_no_patient_prescription(request, patient, disease)
        else:
            prescription_object = self.create_patient_prescription(request, patient_id, disease)

        return prescription_object

    def create_no_patient_prescription(self, request, name, disease):
        health_professional = HealthProfessional.objects.get(email=request.user)
        no_patient_prescription = NoPatientPrescription(health_professional=health_professional,
                                                        patient=name, cid=disease)
        no_patient_prescription.save()

        return no_patient_prescription

    def create_patient_prescription(self, request, patient_id, disease):
        health_professional = HealthProfessional.objects.get(email=request.user)
        patient = Patient.objects.get(pk=patient_id)
        patient_prescription = PatientPrescription(health_professional=health_professional,
                                                   patient=patient, cid=disease)
        patient_prescription.save()

        return patient_prescription

    def create_many_to_many_exam(self, form, exam_prescription, request):
        """
        Defines which type of exam will be added to the prescription and create it.
        """

        exam_type = form.cleaned_data.get('exam_type')
        if exam_type == 'default_exam':
            id_tuss = form.cleaned_data.get('id_tuss')
            self.create_prescription_default_exam(exam_prescription,
                                                  id_tuss)
        elif exam_type == 'custom_exam':
            exam_id = form.cleaned_data.get('exam_id')
            self.create_prescription_custom_exam(exam_prescription,
                                                 exam_id,
                                                 request)
        else:
            # Nothing to do.
            pass

    def create_prescription_default_exam(self, prescription, id_tuss):
        prescription_default_exam_object = PrescriptionDefaultExam(
            prescription=prescription,
            exam=id_tuss
            )
        prescription_default_exam_object.save()

    def create_prescription_custom_exam(self, prescription, exam_id, request):
        # custom_exam = CustomExam.objects.get(pk=exam_id)

        prescription_custom_exam_object = PrescriptionCustomExam(
            prescription=prescription,
            exam=exam_id,
            )

        prescription_custom_exam_object.save()

    def create_prescription_has_manipulated_medicine(self, medicine_id, quantity, posology, prescription_medicine):
        prescription_has_manipulatedmedicine_object = PrescriptionHasManipulatedMedicine(
            manipulated_medicine_id=medicine_id,
            posology=posology, quantity=quantity,
            prescription_medicine=prescription_medicine)

        prescription_has_manipulatedmedicine_object.save()

    def create_prescription_has_medicine(self, medicine_id, quantity, posology, prescription_medicine):
        prescription_has_medicine_object = PrescriptionHasMedicine(
            medicine_id=medicine_id,
            posology=posology, quantity=quantity,
            prescription_medicine=prescription_medicine)

        prescription_has_medicine_object.save()

    def add_medicine_in_prescription(self, atomic_form, prescription_medicine):
        """
        Defines which type of drug will be added to the prescription and adds it.
        """

        medicine_type = atomic_form.cleaned_data.get('medicine_type')
        medicine_id = atomic_form.cleaned_data.get('medicine_id')
        quantity = atomic_form.cleaned_data.get('quantity')
        posology = atomic_form.cleaned_data.get('posology')

        if medicine_type == 'medicine':
            self.create_prescription_has_medicine(medicine_id,
                                                  quantity,
                                                  posology,
                                                  prescription_medicine)
        elif medicine_type == 'manipulated_medicine':
            self.create_prescription_has_manipulated_medicine(medicine_id,
                                                              quantity,
                                                              posology,
                                                              prescription_medicine)
        else:
            # Nothing to do.
            pass

    def add_recommendation_in_prescription(self, form_recommendation, prescription_object):
        """
        Add recomendation to prescription.
        """

        recommendation = form_recommendation.cleaned_data.get('recommendation')
        if recommendation is not None:
            prescription_recommendation_object = PrescriptionRecommendation(
                prescription=prescription_object, recommendation=recommendation)

            prescription_recommendation_object.save()

    def get(self, request, *args, **kwargs):
        """
        Rendering form in view.
        """
        prescription_form = CreatePrescriptionForm(request.GET or None)
        form_medicine = self.MedicinePrescriptionFormSet(request.GET or None, prefix='form_medicine')
        form_recommendation = self.RecommendationPrescriptionFormSet(request.GET or None, prefix='form_reccomendation')
        form_exam = self.ExamPrescriptionFormSet(request.GET or None, prefix='form_exam')

        data = dict()
        context = {'prescription_form': prescription_form,
                   'form_medicine': form_medicine,
                   'form_recommendation': form_recommendation,
                   'form_exam': form_exam}
        data['html_form'] = render_to_string(self.template_name, context, request=request)
        # Json to communication Ajax.
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        """
        Save data in the form in database.
        """
        prescription_form = CreatePrescriptionForm(request.POST or None)
        form_medicine = self.MedicinePrescriptionFormSet(request.POST or None, prefix='form_medicine')
        form_recommendation = self.RecommendationPrescriptionFormSet(request.POST or None, prefix='form_reccomendation')
        form_exam = self.ExamPrescriptionFormSet(request.POST or None, prefix='form_exam')
        data = dict()

        # Checks whether the completed forms are valid.
        default_is_valid = False
        atomic_is_valid = False
        form_recommendation_is_valid = False
        form_exam_is_valid = False
        if prescription_form.is_valid():
            default_is_valid = True
            if form_medicine.is_valid():
                atomic_is_valid = True
                prescription_medicine_object = self.create_prescription(prescription_form, request)
                for atomic_form in form_medicine:
                    self.add_medicine_in_prescription(atomic_form, prescription_medicine_object)

                if form_recommendation.is_valid():
                    form_recommendation_is_valid = True
                    for recommendation_field in form_recommendation:
                        self.add_recommendation_in_prescription(recommendation_field, prescription_medicine_object)

                    if form_exam.is_valid():
                        form_exam_is_valid = True
                        for exam_atomic_form in form_exam:
                            self.create_many_to_many_exam(exam_atomic_form, prescription_medicine_object, request)
                    else:
                        # Nothing to do.
                        pass
                else:
                    # Nothing to do.
                    pass
            else:
                # Nothing to do.
                pass
        else:
            # Nothing to do.
            pass

        # Verify if all forms are valids.
        data['form_is_valid'] = default_is_valid and atomic_is_valid and form_recommendation_is_valid
        data['form_is_valid'] = data['form_is_valid'] and form_exam_is_valid

        context = {'prescription_form': prescription_form,
                   'form_medicine': form_medicine,
                   'form_recommendation': form_recommendation,
                   'form_exam': form_exam}
        data['html_form'] = render_to_string(self.template_name, context, request=request)
        # Json to communication Ajax.
        return JsonResponse(data)
