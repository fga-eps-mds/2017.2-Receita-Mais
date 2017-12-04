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
from user import constants
from user.views import AddPatientView

# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


# This class makes the patient register.
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

        # Defining the email field with the invitated patient email.
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'user_email': patient.email})

    def post(self, request, activation_key, *args, **kwargs):
        logger.debug("Start post method.")

        try:
            patient_profile = SendInvitationProfile.objects.get(activation_key=activation_key)
            patient = patient_profile.patient
        except:
            messages.success(
                request, 'Não há convites para esta conta!', extra_tags='alert')
            return redirect('/')

        # Time to register expirated.
        if patient_profile.key_expires < timezone.now():
            messages.success(
                request, 'Tempo de registro expirado!', extra_tags='alert')
            return redirect('/')

        patient_form = self.form_class(request.POST)

        if patient_form.is_valid():
            RegisterPatientView.register_patient(patient, patient_form,
                                                 patient_profile)
            messages.success(
                request, 'Registro Realizado!', extra_tags='alert')
            return redirect('/user/login_patient/')

        return render(request, self.template_name, {'form': patient_form, 'user_email': patient.email})

    # Making the register of the invited patient informations in database.
    def register_patient(patient, patient_form, patient_profile):
        patient.name = patient_form.cleaned_data.get('name')
        patient.sex = patient_form.cleaned_data.get('sex')
        patient.phone = patient_form.cleaned_data.get('phone')
        patient.date_of_birth = patient_form.cleaned_data.get('date_of_birth')
        patient.CPF_document = patient_form.cleaned_data.get('CPF_document')
        patient.CEP = patient_form.cleaned_data.get('CEP')
        patient.UF = patient_form.cleaned_data.get('UF')
        patient.city = patient_form.cleaned_data.get('city')
        patient.neighborhood = patient_form.cleaned_data.get('neighborhood')
        patient.complement = patient_form.cleaned_data.get('complement')

        password = patient_form.cleaned_data.get('password')
        patient.set_password(password)
        patient.is_active = True
        patient.save()

        patient_profile.delete()
        AddPatientView.activate_link_patient_health_professional(patient.email)

        logger.debug("Exit post method - Successful user registration.")
        logger.debug("Exit post method - Not successful user registration.")
