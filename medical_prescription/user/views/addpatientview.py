# standard library
import hashlib
import random
import datetime

# Django
from django.views.generic import FormView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone

# Local Django
from user import constants
from user.forms import AddPatientForm
from user.models import (Patient,
                         HealthProfessional,
                         SendInvitationProfile,
                         AssociatedHealthProfessionalAndPatient)

from user.views import SendMail


class AddPatientView(FormView):
    """
    This class is responsible for link patients and health professionals.
    """

    form_class = AddPatientForm
    template_name = 'add_patient.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        actual_user = request.user

        if form.is_valid():
            # Preparing the informations necessary to make the especific link procedures.
            email = form.cleaned_data.get('email')
            email_from_database_health_professional = HealthProfessional.objects.filter(email=email)

            if email_from_database_health_professional.exists():
                message = constants.ALERT_HEALTH_PROFESSIONAL
                messages.info(request, message, extra_tags='alert')
                return render(request, self.template_name, {'form': form})

            email_from_database = Patient.objects.filter(email=email)
            health_professional_profile = HealthProfessional.objects.get(email=actual_user.email)

            if email_from_database.exists():
                patient_profile = Patient.objects.get(email=email)
                relationship_database = AssociatedHealthProfessionalAndPatient.objects.filter(associated_patient=patient_profile,
                                                                                              associated_health_professional=health_professional_profile)

                if relationship_database.exists():
                    message = AddPatientView.relationship_exists(patient_profile, health_professional_profile)
                    messages.info(request, message, extra_tags='alert')
                    return redirect('/user/listlinkedpatients/')
                else:
                    message = AddPatientView.relationship_does_not_exist(patient_profile,
                                                                         health_professional_profile)
                    messages.info(request, message, extra_tags='alert')
                    return redirect('/user/listlinkedpatients/')

            else:
                message = AddPatientView.patient_does_not_exist(email,
                                                                health_professional_profile)
                messages.info(request, message, extra_tags='alert')
                return render(request, self.template_name, {'form': form})

        else:
            # Nothing to do.
            pass

        return render(request, self.template_name, {'form': form})

    # If link between users already exists.
    def relationship_exists(patient_profile, health_professional_profile):
        if patient_profile.is_active:
            message = constants.LINKED_PATIENT_EXISTS
        else:
            message = AddPatientView.profile_is_not_active(patient_profile, health_professional_profile)

        return message

    # If link between users doesn't yet exist.
    def relationship_does_not_exist(patient_profile, health_professional_profile):

        # Link between the users is created.
        AddPatientView.create_link_patient_health_professional(health_professional_profile,
                                                               patient_profile)

        if patient_profile.is_active:
            relationship = AssociatedHealthProfessionalAndPatient.objects.get(associated_health_professional=health_professional_profile,
                                                                              associated_patient=patient_profile)
            relationship.is_active = True
            relationship.save()
            message = constants.LINKED_PATIENT_SUCESS
        else:
            message = AddPatientView.profile_is_not_active(patient_profile, health_professional_profile)

        return message

    # Sending a new e-mail and updating key expires.
    def profile_is_not_active(patient_profile, health_professional_profile):
        profile = SendInvitationProfile.objects.get(patient=patient_profile)
        profile.key_expires = timezone.now() + datetime.timedelta(days=2)
        profile.save()
        AddPatientView.send_invitation_email(patient_profile.email, profile, health_professional_profile)
        message = constants.SENDED_EMAIL

        return message

    # Creating a temporary profile.
    def patient_does_not_exist(email, health_professional_profile):
        send_invitation_profile = AddPatientView.create_send_invitation_profile(email)
        patient_profile = Patient.objects.get(email=email)
        AddPatientView.create_link_patient_health_professional(health_professional_profile,
                                                               patient_profile)
        AddPatientView.send_invitation_email(email, send_invitation_profile, health_professional_profile)

        message = constants.SENDED_EMAIL

        return message

    # Prepare the information needed to send invitation and to make link between the users.
    def create_send_invitation_profile(email):
        salt = hashlib.sha1(str(random.random()).
                            encode('utf-8')).hexdigest()[:5]
        activation_key = hashlib.sha1(str(salt+email).
                                      encode('utf‌​-8')).hexdigest()
        key_expires = timezone.now() + datetime.timedelta(days=2)

        patient = Patient(email=email)
        patient.save()

        # Creating the temporary profile.
        new_profile = SendInvitationProfile(patient=patient,
                                            activation_key=activation_key,
                                            key_expires=key_expires)
        new_profile.save()

        return new_profile

    # Sending invitation email.
    def send_invitation_email(email, SendInvitationProfile, HealthProfessional):
        SendMail(email, HealthProfessional, SendInvitationProfile).start()

    # This method is responsible for create the link between the users.
    def create_link_patient_health_professional(HealthProfessional, Patient):
        link = AssociatedHealthProfessionalAndPatient(associated_health_professional=HealthProfessional,
                                                      associated_patient=Patient)
        link.save()

    # Activating the link between the users.
    def activate_link_patient_health_professional(email):
        patient_from_database = Patient.objects.filter(email=email)

        if patient_from_database.exists():
            patient_profile = Patient.objects.get(email=email)
            AssociatedHealthProfessionalAndPatient.objects.filter(associated_patient=patient_profile).update(is_active=True)
