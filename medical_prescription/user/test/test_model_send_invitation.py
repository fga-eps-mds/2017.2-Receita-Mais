# Standard library
import hashlib
import random
import datetime

# Django imports
from django.test import TestCase

# Local django imports
from user.models import SendInvitationProfile, Patient


class TestSendInvitationProfile(TestCase):

    def setUp(self):
        self.send_invitation_profile = SendInvitationProfile()
        self.patient = Patient.objects.create_user(email='patient@patient.com')
        self.salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
        self.activation_key = hashlib.sha1(str(self.salt+self.patient.email).encode('utf‌​-8')).hexdigest()
        self.key_expires = datetime.datetime.today() + datetime.timedelta(2)
        self.send_invitation_profile = SendInvitationProfile.objects.create(activation_key=self.activation_key,
                                                                            patient=self.patient,
                                                                            key_expires=self.key_expires)

    def test_user_str(self):

        self.assertEquals(str(self.send_invitation_profile), 'patient@patient.com',)
