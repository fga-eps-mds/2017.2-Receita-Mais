# Django
from django.template.loader import render_to_string
from django.http import JsonResponse

# Local Django
from prescription.views import CreatePrescriptionView
from prescription.forms import (CreatePrescriptionForm)


class CreateCopyPrescription(CreatePrescriptionView):

    # Rendering form view.
    def get(self, request, *args, **kwargs):

        prescription_form = CreatePrescriptionForm(request.GET or None)

        # Save objects of fields in database.
        form_medicine = self.MedicinePrescriptionFormSet(request.GET or None, prefix='form_medicine')
        form_recommendation = self.RecommendationPrescriptionFormSet(request.GET or None, prefix='form_reccomendation')
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
