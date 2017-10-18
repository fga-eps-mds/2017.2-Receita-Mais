from django.shortcuts import render, redirect
from django.views.generic import FormView

from prescription.forms import CreatePrescriptionExamForm


# Create your views here.

class CreatePrescriptionView(FormView):
    template_name = 'createprescriptionexam.html'
    form_class = CreatePrescriptionExamForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            patient = form.cleaned_data.get('patient')
            cid = form.cleaned_data.get('cid')
            exam = form.cleaned_data.get('exam')

            return redirect('/dashboard_health_professional/health_professional')
        else:
            return render(request, self.template_name, {'form': form})
