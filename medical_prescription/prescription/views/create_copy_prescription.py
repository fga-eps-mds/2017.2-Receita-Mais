# Django
from django.template.loader import render_to_string
from django.http import JsonResponse

# Local Django
from prescription.views import CreatePrescriptionView
from prescription.forms import (CreatePrescriptionForm)
from prescription.models import (Prescription,
                                 PrescriptionHasMedicine,
                                 PrescriptionHasManipulatedMedicine,
                                 NoPatientPrescription,
                                 PatientPrescription
                                 )


class CreateCopyPrescription(CreatePrescriptionView):
    """
    Edit prescription copy.
    """
    template_name = 'create_prescription_copy.html'

    # Get Prescritption.
    def get(self, request, *args, **kwargs):

        prescription_base = Prescription.objects.get(pk=self.kwargs['pk'])

        # Try to get an NoPatientPrescription prescription if does not have raise a exception.
        try:
            specialize_prescription = NoPatientPrescription.objects.get(prescription_ptr=prescription_base)
        except:
            specialize_prescription = None

        if specialize_prescription is None:
            specialize_prescription = PatientPrescription.objects.get(prescription_ptr=prescription_base)

            if specialize_prescription.cid is not None:
                prescription_form = CreatePrescriptionForm(request.GET or None, initial={
                    'cid': specialize_prescription.cid.description,
                    'cid_id': specialize_prescription.cid.pk
                })
            else:
                prescription_form = CreatePrescriptionForm(request.GET or None)
        else:
            if specialize_prescription.cid is not None:
                prescription_form = CreatePrescriptionForm(request.GET or None, initial={
                    'cid': specialize_prescription.cid.description,
                    'cid_id': specialize_prescription.cid.pk
                })
            else:
                prescription_form = CreatePrescriptionForm(request.GET or None)

        # Save objects of fields in database.
        form_medicine = self.get_initial_medicine_formset(prescription_base, request)
        form_recommendation = self.get_initial_recommendation_formset(prescription_base, request)
        form_exam = self.get_initial_exam_formset(prescription_base, request)

        # Get context.
        data = dict()
        context = {'prescription_form': prescription_form,
                   'form_medicine': form_medicine,
                   'form_recommendation': form_recommendation,
                   'form_exam': form_exam,
                   }

        data['html_form'] = render_to_string(self.template_name, context, request=request)
        # Json to communication Ajax.
        return JsonResponse(data)

    # Get context data of Medicine in Prescription.
    def get_initial_medicine_formset(self, prescription, request):
        medicine_models = PrescriptionHasMedicine.objects.filter(prescription_medicine=prescription)
        context = []
        for medicine in medicine_models:
            medicine_context = {
                'medicine': medicine.medicine.name,
                'medicine_id': medicine.medicine.pk,
                'medicine_type': 'medicine',
                'quantity': medicine.quantity,
                'via': medicine.via,
                'posology': medicine.posology,
                }
            context.append(medicine_context)
        manipulated_medicine_models = PrescriptionHasManipulatedMedicine.objects.filter(
            prescription_medicine=prescription
            )

        for manipulated_medicine in manipulated_medicine_models:
            manipulated_medicine_context = {
                'medicine': manipulated_medicine.manipulated_medicine.recipe_name,
                'medicine_id': manipulated_medicine.manipulated_medicine.pk,
                'medicine_type': 'manipulated_medicine',
                'quantity': manipulated_medicine.quantity,
                'via': manipulated_medicine.via,
                'posology': manipulated_medicine.posology,
                }
            context.append(manipulated_medicine_context)
        # Adding a initial context with medications and return the formset.
        return self.MedicinePrescriptionFormSet(request.GET or None, initial=context, prefix='form_medicine')

    # Get context data of Exams in Prescription.
    def get_initial_exam_formset(self, prescription, request):
        context = []
        for default_exam in prescription.default_exams.all():
            default_exam_context = {
                'exam': default_exam.description,
                'exam_id': default_exam.pk,
                'exam_type': 'default_exam',
                }
            context.append(default_exam_context)

        for custom_exam in prescription.custom_exams.all():
            custom_exam_context = {
                'exam': custom_exam.description,
                'exam_id': custom_exam.pk,
                'exam_type': 'custom_exam',
                }
            context.append(custom_exam_context)

        for new_exam in prescription.new_exams.all():
            new_exam_context = {
                'exam': new_exam.exam_description,
                'exam_id': new_exam.pk,
                'exam_type': 'new_exams',
                }
            context.append(new_exam_context)
        # Adding a initial context with exams and return the formset.
        return self.ExamPrescriptionFormSet(request.GET or None, initial=context, prefix='form_exam')

    # Get context data of Recommendation in Prescription.
    def get_initial_recommendation_formset(self, prescription, request):
        context = []
        for recommendation in prescription.new_recommendations.all():
            recommendation_context = {
                'recommendation': recommendation.recommendation_description,
                }
            context.append(recommendation_context)

        for recommendation in prescription.custom_recommendations.all():
            recommendation_context = {
                'recommendation': recommendation.recommendation,
                }
            context.append(recommendation_context)
        # Adding a initial context with recommendation and return the formset.
        return self.RecommendationPrescriptionFormSet(request.GET or None,
                                                      initial=context,
                                                      prefix='form_recommendation')
