from django.test import TestCase

from user.models import User
from user.forms import ConfirmPasswordForm


class TestConfirmPasswordForm(TestCase):

    def setUp(self):

        self.email_valid_reset = 'admin@gmail.com'
        self.email_valid = 'admin@admin.com'
        self.email_invalid = 'admin.com'
        self.email_invalid_1 = 'admin@hotmail.com'

        self.password_invalid_match = '1234568'
        self.password_valid = '1234567'
        self.password_invalid_MAX = '1234567891011'
        self.password_invalid_MIN = '123'

        user = User()
        user.email = "admin@hotmail.com"
        user.save()

    def test_user_password_confirmation_form_valid(self):
        form_data = {'password': self.password_valid,
                     'password_confirmation': self.password_valid}
        form = ConfirmPasswordForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_password_confirmation_form_invalid_match(self):
        form_data = {'password': self.password_valid,
                     'password_confirmation': self.password_invalid_match}
        form = ConfirmPasswordForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_password_confirmation_form_invalid(self):
        form_data = {'password': self.password_invalid_MAX,
                     'password_confirmation': self.password_invalid_MIN}
        form = ConfirmPasswordForm(data=form_data)
        self.assertFalse(form.is_valid())
