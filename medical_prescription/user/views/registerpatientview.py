# standard library
import logging

# Django
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib import messages

# Local Django
from user.models import Patient
from user.forms import PatientForm
from user.views import ConfirmAccountView
from user import constants

# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class RegisterPatientView(FormView):
    form_class = PatientForm
    template_name = 'register_patient.html'

    def get(self, request, *args, **kwargs):
        logger.debug("Start get method.")
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        logger.debug("Start post method.")
        patient_form = self.form_class(request.POST)

        if patient_form.is_valid():
            email = patient_form.cleaned_data.get('email')
            password = patient_form.cleaned_data.get('password')
            name = patient_form.cleaned_data.get('name')
            sex = patient_form.cleaned_data.get('sex')
            phone = patient_form.cleaned_data.get('phone')
            date_of_birth = patient_form.cleaned_data.get('date_of_birth')
            CPF_document = patient_form.cleaned_data.get('CPF_document')
            CEP = patient_form.cleaned_data.get('CEP')
            UF = patient_form.cleaned_data.get('UF')
            city = patient_form.cleaned_data.get('city')
            neighborhood = patient_form.cleaned_data.get('neighborhood')
            complement = patient_form.cleaned_data.get('complement')

            Patient.objects.create_user(email=email, password=password, name=name,
                                        sex=sex, date_of_birth=date_of_birth,
                                        phone=phone, CPF_document=CPF_document,
                                        CEP=CEP, UF=UF, city=city,
                                        neighborhood=neighborhood, complement=complement)

            logger.debug("Exit post method - Successful user registration.")
            logger.debug("Exit post method - Not successful user registration.")

            ConfirmAccountView.activate_account_request(email)

            messages.success(
                request, 'Registro Realizado!Um email foi enviado com seu link para ativação!', extra_tags='alert')

            return redirect('/')

        return render(request, self.template_name, {'form': patient_form})
