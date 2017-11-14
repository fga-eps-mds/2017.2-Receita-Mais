# Django
from django.views.generic import DetailView
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


class CreatePrescriptionView(DetailView):
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
