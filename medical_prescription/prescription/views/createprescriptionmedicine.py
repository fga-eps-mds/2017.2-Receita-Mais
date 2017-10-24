# Django
from django.views.generic import FormView
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.forms import formset_factory


# Local Django
from prescription.forms import (CreatePrescriptionForm,
                                MedicinePrescriptionForm
                                )


class CreatePrescriptionMedicine(FormView):
    """
    Responsible for rendering to fields.
    """
    template_name = 'show_prescription_medicine.html'
    # Defines that this form will have multiple instances.
    MedicinePrescriptionFormSet = formset_factory(MedicinePrescriptionForm)

    def get(self, request, *args, **kwargs):
        """
        Rendering form in view.
        """
        form = CreatePrescriptionForm(request.GET or None)
        formset = self.MedicinePrescriptionFormSet(request.GET or None)

        data = dict()
        context = {'form': form,
                   'formset': formset}
        data['html_form'] = render_to_string(self.template_name, context, request=request)
        # Json to communication Ajax.
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        """
        Save data in the form in database.
        """
        form = CreatePrescriptionForm(request.POST or None)
        formset = self.MedicinePrescriptionFormSet(request.POST or None)
        data = dict()

        # Checks whether the completed forms are valid.
        if form.is_valid():
            print(form.cleaned_data)
        for atomic_form in formset:
            if atomic_form.is_valid():
                print(atomic_form.cleaned_data)

        context = {'form': form,
                   'formset': formset}
        data['html_form'] = render_to_string(self.template_name, context, request)
        # Json to communication Ajax.
        return JsonResponse(data)
