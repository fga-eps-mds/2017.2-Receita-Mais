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
                                 PrescriptionDefaultExam,
                                 PrescriptionCustomExam,
                                 PrescriptionNewExam,
                                 PrescriptionNewRecommendation,
                                 PrescriptionCustomRecommendation,
                                 PatientPrescription,
                                 NoPatientPrescription
                                 )
from exam.models import DefaultExam, CustomExam, NewExam
from disease.models import Disease
from recommendation.models import NewRecommendation, CustomRecommendation
from user.models import (Patient,
                         HealthProfessional,
                         AssociatedHealthProfessionalAndPatient
                         )
from user.views import AddPatientView


class CreatePrescriptionView(FormView):
    """
        Responsible for rendering to fields.
    """
    template_name = 'show_prescription_medicine.html'
    message = None

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
        patient_name = form.cleaned_data.get('patient')
        patient_email = form.cleaned_data.get('email')
        cid_id = form.cleaned_data.get('cid_id')

        if cid_id is not None:
            disease = Disease.objects.get(pk=cid_id)
        else:
            disease = None

        if self.check_relation(patient_email, request):
            prescription_object = self.create_patient_prescription(request, patient_email, patient_name, disease)
        else:
            prescription_object = self.create_no_patient_prescription(request, patient_name, disease)

        return prescription_object

    def check_relation(self, patient_email, request):

        """
        Creating link between users if it doesn't exist.
        """

        health_professional = request.user.healthprofessional

        if patient_email:
            patient_from_database = Patient.objects.filter(email=patient_email)

            if patient_from_database.exists():
                patient = Patient.objects.get(email=patient_email)
                link = AssociatedHealthProfessionalAndPatient.objects.filter(associated_health_professional=health_professional,
                                                                             associated_patient=patient)
                if link.exists() and link.first():
                    return True
                elif link.exists() and not link.first():
                    message = AddPatientView.relationship_exists(patient, health_professional)
                    self.set_message(patient, message)
                else:
                    message = AddPatientView.relationship_does_not_exist(patient, health_professional)
                    self.set_message(patient, message)
            else:
                message = AddPatientView.patient_does_not_exist(patient_email, health_professional)
                self.set_message(None, message)
        else:
            return False

        return True

    def create_no_patient_prescription(self, request, name, disease):
        health_professional = HealthProfessional.objects.get(email=request.user)
        no_patient_prescription = NoPatientPrescription(health_professional=health_professional,
                                                        patient=name, cid=disease)
        no_patient_prescription.save()

        return no_patient_prescription

    def create_patient_prescription(self, request, patient_email, patient_name, disease):
        health_professional = HealthProfessional.objects.get(email=request.user)
        patient = Patient.objects.get(email=patient_email)
        patient_prescription = PatientPrescription(health_professional=health_professional,
                                                   patient=patient, name=patient_name,
                                                   cid=disease)
        patient_prescription.save()

        return patient_prescription

    def create_many_to_many_exam(self, form, exam_prescription, request):
        """
        Defines which type of exam will be added to the prescription and create it.
        """

        exam_type = form.cleaned_data.get('exam_type')

        if exam_type is not None:

            if exam_type == 'default_exam':
                id_tuss = form.cleaned_data.get('exam_id')
                self.create_prescription_default_exam(exam_prescription,
                                                      id_tuss)
            elif exam_type == 'custom_exam':
                exam_id = form.cleaned_data.get('exam_id')
                self.create_prescription_custom_exam(exam_prescription,
                                                     exam_id,
                                                     request)

            else:
                exam_id = form.cleaned_data.get('exam')
                self.create_prescription_new_exam(exam_prescription,
                                                  exam_id,
                                                  request)
        else:
            # Nothing to do.
            pass

    def create_prescription_default_exam(self, prescription, exam_id):
        default_exam = DefaultExam.objects.get(pk=exam_id)
        prescription_default_exam_object = PrescriptionDefaultExam(
            prescription=prescription,
            exam=default_exam
            )
        prescription_default_exam_object.save()

    def create_prescription_custom_exam(self, prescription, exam_id, request):
        custom_exam = CustomExam.objects.get(pk=exam_id)

        prescription_custom_exam_object = PrescriptionCustomExam(
            prescription=prescription,
            exam=custom_exam,
            )

        prescription_custom_exam_object.save()

    def create_prescription_new_exam(self, prescription, exam_text, request):
        new_exam = NewExam(exam_description=exam_text)
        new_exam.save()
        prescription_new_exam_object = PrescriptionNewExam(
            prescription=prescription,
            exam=new_exam,
            )

        prescription_new_exam_object.save()

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

    def create_prescription_custom_recommendation(self, prescription, recommendation_id):
        custom_recommendation = CustomRecommendation.objects.get(pk=recommendation_id)

        prescription_custom_recommendation_object = PrescriptionCustomRecommendation(
            prescription=prescription,
            recommendation=custom_recommendation,
            )

        prescription_custom_recommendation_object.save()

    def create_prescription_new_recommendation(self, prescription, recommendation_text, request):
        new_recommendation = NewRecommendation(recommendation_description=recommendation_text)
        new_recommendation.save()
        prescription_new_recommendation_object = PrescriptionNewRecommendation(
            prescription=prescription,
            recommendation=new_recommendation,
            )

        prescription_new_recommendation_object.save()

    def add_recommendation_in_prescription(self, form_recommendation, prescription_object, request):
        """
        Add recomendation to prescription.
        """

        recommendation = form_recommendation.cleaned_data.get('recommendation')
        recommendation_id = form_recommendation.cleaned_data.get('recommendation_id')
        recommendation_type = form_recommendation.cleaned_data.get('recommendation_type')

        if recommendation is not None:
            if recommendation_type == 'custom_recommendation':
                self.create_prescription_custom_recommendation(prescription_object,
                                                               recommendation_id)
            else:
                self.create_prescription_new_recommendation(prescription_object,
                                                            recommendation,
                                                            request)
        else:
            # Nothing to do.
            pass

    # Rendering form view.
    def get(self, request, *args, **kwargs):

        prescription_form = CreatePrescriptionForm(request.GET or None)

        # Save objects of fields in database.
        form_medicine = self.MedicinePrescriptionFormSet(request.GET or None, prefix='form_medicine')
        form_recommendation = self.RecommendationPrescriptionFormSet(request.GET or None, prefix='form_recommendation')
        form_exam = self.ExamPrescriptionFormSet(request.GET or None, prefix='form_exam')

        # Get context.
        data = dict()
        context = {'prescription_form': prescription_form,
                   'form_medicine': form_medicine,
                   'form_recommendation': form_recommendation,
                   'form_exam': form_exam}

        data['html_form'] = render_to_string(self.template_name, context, request=request)
        # Json to communication Ajax.
        return JsonResponse(data)

    # Save data in the form in database.
    def post(self, request, *args, **kwargs):

        prescription_form = CreatePrescriptionForm(request.POST or None)

        # Save objcts of fields in database.
        form_medicine = self.MedicinePrescriptionFormSet(request.POST or None, prefix='form_medicine')
        form_recommendation = self.RecommendationPrescriptionFormSet(request.POST or None, prefix='form_recommendation')
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
                data['id_prescription'] = prescription_medicine_object.id

                for atomic_form in form_medicine:
                    self.add_medicine_in_prescription(atomic_form, prescription_medicine_object)

                if form_recommendation.is_valid():
                    form_recommendation_is_valid = True
                    for recommendation_field in form_recommendation:
                        print(recommendation_field)
                        self.add_recommendation_in_prescription(recommendation_field, prescription_medicine_object, request)

                    # Verirfy exam and adding fields in prescription.
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

        print(data['form_is_valid'])
        self.get_message(data)
        # Json to communication Ajax.
        return JsonResponse(data)

    def set_message(self, patient, message_body):
        if patient:
            self.message = ({'message': message_body,
                             'image': patient.image_profile.url,
                             'name': patient.name})
        else:
            self.message = ({'message': message_body})

    def get_message(self, data):
        if self.message:
            data['message'] = self.message
            self.message = None
        else:
            # Nothing to do.
            pass
