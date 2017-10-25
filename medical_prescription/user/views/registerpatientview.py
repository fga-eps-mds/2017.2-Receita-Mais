# standard library
import logging

# Django
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.utils import timezone
from django.contrib import messages

# Local Django
from user.models import SendInvitationProfile
from user.forms import PatientForm
from user.views import ConfirmAccountView
from user import constants

# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class RegisterPatientView(FormView):
    form_class = PatientForm
    template_name = 'register_patient.html'

    def get(self, request, *args, activation_key, **kwargs):
        logger.debug("Start get method.")

        try:
            patient_profile = SendInvitationProfile.objects.get(activation_key=activation_key)
            patient = patient_profile.patient
        except:
            messages.success(
                request, 'Não há convites para esta conta!', extra_tags='alert')
            return redirect('/')

        form = self.form_class(initial=self.initial)
        form.fields["email"].initial = patient.email
        form.fields['email'].widget.attrs['readonly'] = True
        return render(request, self.template_name, {'form': form})

    def post(self, request, activation_key, *args, **kwargs):
        logger.debug("Start post method.")

        try:
            patient_profile = SendInvitationProfile.objects.get(activation_key=activation_key)
            patient = patient_profile.patient
        except:
            messages.success(
                request, 'Não há convites para esta conta!', extra_tags='alert')
            return redirect('/')

        if patient_profile.key_expires < timezone.now():
            messages.success(
                request, 'Tempo de registro expirado!', extra_tags='alert')
            return redirect('/')

        patient_form = self.form_class(request.POST)

        if patient_form.is_valid():
            RegisterPatientView.register_patient(patient, patient_form,
                                                 patient_profile)
            messages.success(
                request, 'Registro Realizado!Um email foi enviado com seu link para ativação!', extra_tags='alert')
            return redirect('/')

        return render(request, self.template_name, {'form': patient_form})

    def register_patient(patient, patient_form, patient_profile):
        patient.name = patient_form.cleaned_data.get('name')
        patient.sex = patient_form.cleaned_data.get('sex')
        patient.phone = patient_form.cleaned_data.get('phone')
        patient.date_of_birth = patient_form.cleaned_data.get('date_of_birth')
        patient.id_document = patient_form.cleaned_data.get('id_document')

        password = patient_form.cleaned_data.get('password')
        patient.set_password(password)

        patient.is_active = True
        patient.save()
        patient_profile.delete()

        ConfirmAccountView.activate_account_request(patient.email)

        logger.debug("Exit post method - Successful user registration.")
        logger.debug("Exit post method - Not successful user registration.")
