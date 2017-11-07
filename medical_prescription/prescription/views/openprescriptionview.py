from django.shortcuts import render
from django.views.generic import View


class OpenPrescriptionView(View):
    """
    Render template with the modal's divs.
    """
    template_name = 'createprescriptionexam.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
