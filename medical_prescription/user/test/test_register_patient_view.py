# Standard library
import hashlib
import random

# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from unittest.mock import patch, MagicMock
from user.models import Patient, SendInvitationProfile
from django.contrib.messages.storage.fallback import FallbackStorage

# Local django imports
from user.views import RegisterPatientView


class RegisterPatientViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.patient = Patient.objects.create_user(email='patient@patient.com', password='senha12')
        self.salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
        self.activation_key = hashlib.sha1(str(self.salt+self.patient.email).encode('utf‌​-8')).hexdigest()
        self.send_invitation_profile = SendInvitationProfile.objects.create(activation_key=self.activation_key,
                                                                            patient=self.patient)

        self.name_valid = 'Teste Nome'
        self.name_invalid = 'Te'
        self.date_of_birth_valid = '10/12/1990'
        self.phone_valid = '1234567890'
        self.email_valid = 'admin@admin.com'
        self.sex_valid = 'M'
        self.id_document_valid = '12345678910'
        self.password_valid = '1234567'

    def test_get(self):
        request = self.factory.get('user/register_patient/(?P<activation_key>\w+)/')
        request.user = AnonymousUser()

        response = RegisterPatientView.as_view()(request, activation_key=self.activation_key)
        self.assertEqual(response.status_code, 200)

    @patch('user.models.Patient.save', MagicMock(name="save"))
    def test_post(self):

        # Create the request
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        request = self.factory.post('/user/register_patient/(?P<activation_key>\w+)/', context)
        setattr(request, 'session', {})
        setattr(request, '_messages', FallbackStorage(request))
        request.user = AnonymousUser()

        # Get the response
        response = RegisterPatientView.as_view()(request, activation_key=self.activation_key)
        self.assertEqual(response.status_code, 302)
