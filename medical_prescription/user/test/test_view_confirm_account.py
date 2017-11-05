# Standard library
import hashlib
import random
import datetime

# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from user.models import Patient, SendInvitationProfile
from django.contrib.messages.storage.fallback import FallbackStorage

# Local django imports
from user.views import ConfirmAccountView


class ConfirmAccountViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.email = 'teste@teste.com'
        self.salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
        self.activation_key = hashlib.sha1(str(self.salt+self.email).encode('utf‌​-8')).hexdigest()
        self.key_expires = datetime.datetime.today() + datetime.timedelta(2)
        self.patient = Patient(email=self.email)
        self.patient.save()
        self.patient_profile = SendInvitationProfile.objects.create(activation_key=self.activation_key,
                                                                    patient=self.patient,
                                                                    key_expires=self.key_expires)
        self.email_invalid = 'invalid@invalid.com'
        self.another_activation_key = hashlib.sha1(str(self.salt+self.email_invalid).encode('utf‌​-8')).hexdigest()

    def test_user_user_get(self):
        request = self.factory.get('user/confirm/(?P<activation_key>\w+)/')
        request.user = AnonymousUser()
        setattr(request, 'session', {})
        setattr(request, '_messages', FallbackStorage(request))
        response = ConfirmAccountView.activate_register_user(request, activation_key=self.activation_key)
        self.assertEqual(response.status_code, 302)

    def test_user_user_get_without_invitation(self):
        '''
        this method tests when the user tryes to register a not invited patient.
        '''
        request = self.factory.get('user/confirm/(?P<activation_key>\w+)/')
        request.user = AnonymousUser()
        setattr(request, 'session', {})
        setattr(request, '_messages', FallbackStorage(request))
        response = ConfirmAccountView.activate_register_user(request, activation_key=self.another_activation_key)
        self.assertEqual(response.status_code, 302)
