# Standard library
import hashlib
import random

# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from unittest.mock import patch, MagicMock
from user.models import Patient, SendInvitationProfile, HealthProfessional
from django.contrib.messages.storage.fallback import FallbackStorage

# Local django imports
from user.views import RegisterPatientView


class AddPatientViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.patient = Patient.objects.create_user(email='patient@patient.com', password='senha12')
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com', password='senha12')
        self.salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
        self.activation_key = hashlib.sha1(str(self.salt+self.patient.email).encode('utf‌​-8')).hexdigest()
        self.send_invitation_profile = SendInvitationProfile.objects.create(activation_key=self.activation_key,
                                                                            patient=self.patient)
        self.email_invalid = "a@a"

    def test_get(self):
        request = self.factory.get('user/addpatient/')
        request.user = self.health_professional

        response = RegisterPatientView.as_view()(request, activation_key=self.activation_key)
        self.assertEqual(response.status_code, 200)

    @patch('user.models.Patient.save', MagicMock(name="save"))
    def test_post(self):

        # Create the request
        context = {'email': self.patient.email}

        request = self.factory.post('/user/addpatient/', context)
        setattr(request, 'session', {})
        setattr(request, '_messages', FallbackStorage(request))
        request.user = self.health_professional

        # Get the response
        response = RegisterPatientView.as_view()(request, activation_key=self.activation_key)
        self.assertEqual(response.status_code, 302)

    def test_post_invalid(self):

        # Create the request
        context = {'email': self.patient.email}

        request = self.factory.post('/user/addpatient/', context)
        setattr(request, 'session', {})
        setattr(request, '_messages', FallbackStorage(request))
        request.user = self.health_professional

        # Get the response
        response = RegisterPatientView.as_view()(request, activation_key=self.activation_key)
        self.assertEqual(response.status_code, 302)
