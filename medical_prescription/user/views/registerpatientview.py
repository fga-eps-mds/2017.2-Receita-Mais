# Django
from django.shortcuts import render
from django.views.generic import FormView

# Local Django
from user.models import Patient
from user.forms import PatientForm


class RegisterPatientView(FormView):
    form_class = PatientForm
    template_name = 'register_patient.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        patient_form = self.form_class(request.POST)

        if patient_form.is_valid():
            email = patient_form.cleaned_data.get('email')
            password = patient_form.cleaned_data.get('password')
            name = patient_form.cleaned_data.get('name')
            sex = patient_form.cleaned_data.get('sex')
            phone = patient_form.cleaned_data.get('phone')
            date_of_birth = patient_form.cleaned_data.get('date_of_birth')
            id_document = patient_form.cleaned_data.get('id_document')

            Patient.objects.create_user(email=email, password=password, name=name,
                                        sex=sex, date_of_birth=date_of_birth,
                                        phone=phone, id_document=id_document)

            ##AQUI

        return render(request, self.template_name, {'form': patient_form})
