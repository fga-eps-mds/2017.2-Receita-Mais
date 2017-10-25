# standard library
import hashlib
import datetime
import random

# Django
from django.views.generic import FormView
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect

# Local Django
from user.forms import AddPatientForm
from user.models import (Patient,
                         HealthProfessional,
                         SendInvitationProfile,
                         AssociatedHealthProfessionalAndPatient)


class AddPatientView(FormView):
    form_class = AddPatientForm
    template_name = 'add_patient.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        actual_user = request.user

        if form.is_valid():
            email = form.cleaned_data.get('email')
            email_from_database = Patient.objects.filter(email=email)
            health_professional_profile = HealthProfessional.objects.get(email=actual_user.email)

            if email_from_database.exists():
                patient_profile = Patient.objects.get(email=email)
                relationship_database = AssociatedHealthProfessionalAndPatient.objects.filter(associated_patient=patient_profile,
                                                                                              associated_health_professional=health_professional_profile)

                if relationship_database.exists():
                    message = AddPatientView.relationship_exists(patient_profile)
                else:
                    message = AddPatientView.relationship_does_not_exist(patient_profile,
                                                                         health_professional_profile)

            else:
                message = AddPatientView.patient_does_not_exist(email,
                                                                health_professional_profile)

        else:
            # Nothing to do.
            pass

        messages.info(request, message, extra_tags='alert')
        return redirect('/')

    def relationship_exists(patient_profile):
        if patient_profile.is_active:
            message = 'O paciente já está adicionado em sua lista de pacientes.'
        else:
            profile = SendInvitationProfile.objects.get(patient=patient_profile)
            AddPatientView.send_invitation_email(patient_profile.email, profile)
            message = 'Um link de cadastro foi enviado ao paciente'

        return message

    def relationship_does_not_exist(patient_profile, health_professional_profile):

        AddPatientView.create_link_patient_health_professional(health_professional_profile,
                                                               patient_profile)

        if patient_profile.is_active:
            AddPatientView.activate_link_patient_health_professional(patient_profile.email)
            message = 'O paciente foi adicionado à sua lista de pacientes.'
        else:
            profile = SendInvitationProfile.objects.get(patient=patient_profile)
            AddPatientView.send_invitation_email(patient_profile.email, profile)
            message = 'Um link de cadastro foi enviado ao paciente'

        return message

    def patient_does_not_exist(email, health_professional_profile):
        send_invitation_profile = AddPatientView.create_send_invitation_profile(email)
        AddPatientView.send_invitation_email(email, send_invitation_profile)
        patient_profile = Patient.objects.get(email=email)
        AddPatientView.create_link_patient_health_professional(health_professional_profile,
                                                               patient_profile)

        message = 'Um link de cadastro foi enviado ao paciente.'

        return message

    def create_send_invitation_profile(email):
        # Prepare the information needed to send the account verification
        # email.
        salt = hashlib.sha1(str(random.random()).
                            encode('utf-8')).hexdigest()[:5]
        activation_key = hashlib.sha1(str(salt+email).
                                      encode('utf‌​-8')).hexdigest()
        key_expires = datetime.datetime.today() + datetime.timedelta(2)

        patient = Patient(email=email)
        patient.save()

        # Creating the temporary user.
        new_profile = SendInvitationProfile(patient=patient,
                                            activation_key=activation_key,
                                            key_expires=key_expires)
        new_profile.save()

        return new_profile

    # Sending email for account activation.
    def send_invitation_email(email, SendInvitationProfile):
        email_subject = 'Convite para Cadastro no Sistema'
        email_body = """
                     Para se cadastrar, clique neste link:
                     http://localhost:8000/user/register_patient/%s
                     """

        send_mail(email_subject, email_body % SendInvitationProfile.activation_key,
                  'medicalprescriptionapp@gmail.com', [email], fail_silently=False)

    def create_link_patient_health_professional(HealthProfessional, Patient):
        link = AssociatedHealthProfessionalAndPatient(associated_health_professional=HealthProfessional,
                                                      associated_patient=Patient)
        link.save()

    def activate_link_patient_health_professional(email):
        patient_profile = Patient.objects.get(email=email)
        AssociatedHealthProfessionalAndPatient.objects.filter(associated_patient=patient_profile).update(is_active=True)
