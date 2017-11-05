import datetime

from django.test import TestCase
from django.test.client import RequestFactory, Client

from user.models import UserActivateProfile, User
from user.views import ConfirmAccountView


class TestUserActivateProfile(TestCase):
    factory = RequestFactory()
    client = Client()
    name_valid = 'Teste Nome'
    date_of_birth_valid = '1990-12-10'
    phone_valid = '1234567890'
    email_valid = 'admin@admin.com'
    sex_valid = 'M'
    id_document_valid = '12345678910'
    password_valid = '1234567'
    crm_valid = '11111'
    crm_state = 'BA'
    user = User()
    key_expires = datetime.datetime.today() + datetime.timedelta(2)
    activation_key = "5c262e9f57ce25652eaefb4ca697191f395f39eb"

    def setUp(self):
        self.user = User.objects.create_user(name=self.name_valid,
                                             date_of_birth=self.date_of_birth_valid,
                                             phone=self.phone_valid,
                                             email=self.email_valid,
                                             sex=self.sex_valid)
        self.new_profile = UserActivateProfile(user=self.user,
                                               key_expires=self.key_expires,
                                               activation_key=self.activation_key)

    def test_user_profile_is_not_null(self):
        self.assertIsNotNone(self.new_profile)

    def test_user_str(self):
        self.assertEqual(self.email_valid, self.new_profile.__str__())


'''
    def test_user_is_activated(self):
        #ConfirmAccountView.activate_register_user(self.activation_key)

        #self.assertTrue(self.user.is_active)
'''
