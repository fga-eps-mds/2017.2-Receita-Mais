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
from user import constants
from user.forms import AddPatientForm
from user.models import (Patient,
                         HealthProfessional,
                         SendInvitationProfile,
                         AssociatedHealthProfessionalAndPatient)


# This class is responsible for link patient and health professional and make
# all the necessary procedures to establish this relationship.
class AddPatientView(FormView):
    form_class = AddPatientForm
    template_name = 'add_patient.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    # This method receives the request made by health_professional to make link
    # between him and the especific patient by email.
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        actual_user = request.user

        if form.is_valid():
            # Preparing the informations necessary to make the especific
            # link procedures.
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
                else:
                    message = AddPatientView.relationship_does_not_exist(patient_profile,
                                                                         health_professional_profile)
                    messages.info(request, message, extra_tags='alert')
                    return redirect('/user/listlinkedpatients/')

            # The patient added for the request health professional does not
            # exist in database, then a temporary profile is created, till he
            # make his registration by email.
            else:
                message = AddPatientView.patient_does_not_exist(email,
                                                                health_professional_profile)
                messages.info(request, message, extra_tags='alert')
                return render(request, self.template_name, {'form': form})

        else:
            # Nothing to do.
            pass

        return render(request, self.template_name, {'form': form})

    # If the patient provided by the health professional exists in databases
    # and there is a relationship between him and health professional,
    # the next steps are made.
    def relationship_exists(patient_profile, health_professional_profile):

        # If the patient is actived, then the relationship between him and
        # health professional already exists. Nothing is made.
        if patient_profile.is_active:
            message = constants.LINKED_PATIENT_EXISTS
        else:
            message = AddPatientView.profile_is_not_active(patient_profile, health_professional_profile)

        return message

    # If the patient provided by the health professional exists in database,
    # but there isn't a relationship between him and the request health
    # professional, the next steps are made.
    def relationship_does_not_exist(patient_profile, health_professional_profile):

        # Link between the users is created.
        AddPatientView.create_link_patient_health_professional(health_professional_profile,
                                                               patient_profile)

        # If the exist patient is actived, then link between him and the
        # request health professional is actived.
        if patient_profile.is_active:
            AssociatedHealthProfessionalAndPatient.objects.get(associated_health_professional=health_professional_profile,
                                                               associated_patient=patient_profile).update(is_active=True)
            message = constants.LINKED_PATIENT_SUCESS
        else:
            message = AddPatientView.profile_is_not_active(patient_profile, health_professional_profile)

        return message

    # If patient is not actived, it means tha he never registered or never
    # activated his account. A new email is sended and his key_expires is
    # updated.
    def profile_is_not_active(patient_profile, health_professional_profile):
        profile = SendInvitationProfile.objects.get(patient=patient_profile)
        profile.key_expires = datetime.datetime.today() + datetime.timedelta(2)
        profile.save()
        AddPatientView.send_invitation_email(patient_profile.email, profile, health_professional_profile)
        message = constants.SENDED_EMAIL

        return message

    # This method calls the methods responsible for create a temporary profile,
    # with an activation_key and a key_expires, for send to patient an
    # invitation email and create the link between the users.
    def patient_does_not_exist(email, health_professional_profile):
        send_invitation_profile = AddPatientView.create_send_invitation_profile(email)
        AddPatientView.send_invitation_email(email, send_invitation_profile, health_professional_profile)
        patient_profile = Patient.objects.get(email=email)
        AddPatientView.create_link_patient_health_professional(health_professional_profile,
                                                               patient_profile)

        message = constants.SENDED_EMAIL

        return message

    def create_send_invitation_profile(email):
        # Prepare the information needed to send invitation and to make link
        # between the users.
        salt = hashlib.sha1(str(random.random()).
                            encode('utf-8')).hexdigest()[:5]
        activation_key = hashlib.sha1(str(salt+email).
                                      encode('utf‌​-8')).hexdigest()
        key_expires = datetime.datetime.today() + datetime.timedelta(2)

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
        email_subject = constants.INVITATION_EMAIL_SUBJECT
        email_body = constants.INVITATION_EMAIL_BODY

        send_mail(email_subject, email_body % (HealthProfessional.name,
                                               SendInvitationProfile.activation_key),
                  'medicalprescriptionapp@gmail.com', [email], fail_silently=False)

    # This method is responsible for create the link between the users.
    def create_link_patient_health_professional(HealthProfessional, Patient):
        link = AssociatedHealthProfessionalAndPatient(associated_health_professional=HealthProfessional,
                                                      associated_patient=Patient)
        link.save()

    # This method is responsible for activate the link between the users and
    # delete the created temporary profile.
    def activate_link_patient_health_professional(email):
        patient_from_database = Patient.objects.filter(email=email)

        if patient_from_database.exists():
            patient_profile = Patient.objects.get(email=email)
            AssociatedHealthProfessionalAndPatient.objects.filter(associated_patient=patient_profile).update(is_active=True)
