# Django
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.template.loader import render_to_string
from django.http import JsonResponse

# Django Local
from prescription.forms import CreatePrescriptionExamForm


class CreateTestePrescriptionView(FormView):
    template_name = 'show_prescription.html'
    form_class = CreatePrescriptionExamForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        data = dict()
        context = {'form': form}
        data['html_show'] = render_to_string(self.template_name, context, request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        data = dict()

        if form.is_valid():
            data['form_is_valid'] = True

        context = {'form': form}
        data['html_form'] = render_to_string(self.template_name, context, request)
        return JsonResponse(data)
