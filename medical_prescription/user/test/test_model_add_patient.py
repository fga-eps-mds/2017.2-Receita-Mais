# Standard library
import hashlib
import random

# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from user.models import Patient, SendInvitationProfile, HealthProfessional, AssociatedHealthProfessionalAndPatient
from django.contrib.messages.storage.fallback import FallbackStorage

# Local django imports
from user.views import AddPatientView


class AddPatientViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.patient = Patient.objects.create_user(email='patient@patient.com', password='senha12')
        self.another_patient = Patient.objects.create_user(email='another@patient.com', password='senha12')
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com', password='senha12')
        self.salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
        self.activation_key = hashlib.sha1(str(self.salt+self.patient.email).encode('utf‌​-8')).hexdigest()
        self.send_invitation_profile = SendInvitationProfile.objects.create(activation_key=self.activation_key,
                                                                            patient=self.patient)
        self.send_another_invitation_profile = SendInvitationProfile.objects.create(activation_key=self.activation_key,
                                                                                    patient=self.another_patient)
        self.relationship_exists = AssociatedHealthProfessionalAndPatient.objects.create(associated_patient=self.another_patient,
                                                                                         associated_health_professional=self.health_professional,
                                                                                         is_active=True)

        self.email_invalid = 'teste.com'
        self.email_valid = 'teste@teste.com'

    def test_user_get(self):
        request = self.factory.get('user/addpatient/')
        request.user = self.health_professional

        response = AddPatientView.as_view()(request, activation_key=self.activation_key)
        self.assertEqual(response.status_code, 200)

    def test_user_post_when_patient_exists_and_its_not_associated(self):
        '''
        This method tests when the email provided by the logged health professional belongs to a
        registered patient, but the patient its not associated with the logged health professional.
        '''
        # Create the request
        context = {'email': self.patient.email}

        request = self.factory.post('/user/addpatient/', context)
        setattr(request, 'session', {})
        setattr(request, '_messages', FallbackStorage(request))
        request.user = self.health_professional

        # Get the response
        response = AddPatientView.as_view()(request, activation_key=self.activation_key)
        self.assertEqual(response.status_code, 302)

    def test_user_post_when_patient_exists_and_its_associated(self):
        '''
        This method tests when the email provided by the logged health professional belongs to a
        registered patient, but the patient alredy is associated with the logged health professional.
        '''
        # Create the request
        context = {'email': self.another_patient.email}

        request = self.factory.post('/user/addpatient/', context)
        setattr(request, 'session', {})
        setattr(request, '_messages', FallbackStorage(request))
        request.user = self.health_professional

        # Get the response
        response = AddPatientView.as_view()(request, activation_key=self.activation_key)
        self.assertEqual(response.status_code, 302)

    def test_user_post_when_patient_not_exists(self):
        '''
        This method tests when the email provided by the logged health professional belongs to a
        unregistered patient.
        '''
        # Create the request
        context = {'email': self.email_valid}

        request = self.factory.post('/user/addpatient/', context)
        setattr(request, 'session', {})
        setattr(request, '_messages', FallbackStorage(request))
        request.user = self.health_professional

        # Get the response
        response = AddPatientView.as_view()(request, activation_key=self.activation_key)
        self.assertEqual(response.status_code, 200)

    def test_user_post_with_invalid_form(self):
        '''
        This method tests when the email provided by the logged health professional is invalid.
        '''
        # Create the request
        context = {'email': self.email_invalid}

        request = self.factory.post('/user/addpatient/', context)
        setattr(request, 'session', {})
        setattr(request, '_messages', FallbackStorage(request))
        request.user = self.health_professional

        # Get the response
        response = AddPatientView.as_view()(request, activation_key=self.activation_key)
        self.assertEqual(response.status_code, 200)

    def test_user_post_health_profesisonal(self):
        '''
        This method tests when the email provided by the logged health professional belongs to a
        registered health professional.
        '''

        # Create the request
        context = {'email': self.health_professional.email}

        request = self.factory.post('/user/addpatient/', context)
        setattr(request, 'session', {})
        setattr(request, '_messages', FallbackStorage(request))
        request.user = self.health_professional

        # Get the response
        response = AddPatientView.as_view()(request, activation_key=self.activation_key)
        self.assertEqual(response.status_code, 200)
