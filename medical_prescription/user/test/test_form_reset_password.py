from django.test import TestCase

from user.models import User
from user.forms import ResetPasswordForm


class TestResetPassword(TestCase):

    def setUp(self):
        self.name_valid = 'Teste Nome'
        self.name_invalid = 'a'

        self.date_of_birth_valid = '10/12/1990'
        self.date_of_birth_invalid = '18'

        self.phone_valid = '123456789'
        self.phone_invalid = '123456789101112'

        self.email_valid_reset = 'admin@gmail.com'
        self.email_valid = 'admin@admin.com'
        self.email_invalid = 'admin.com'
        self.email_invalid_1 = 'admin@hotmail.com'

        self.sex_valid = 'M'
        self.sex_invalid = 'A'

        self.crm_valid = '12345'
        self.crm_invalid = '1'

        self.crm_state_valid = 'DF'
        self.crm_state_invalid = 'asd'

        self.id_document_valid = '12345678910'
        self.id_document_invalid = '1234'

        self.password_valid = '1234567'
        self.password_invalid = '1234567891011'

        user = User()
        user.email = "admin@hotmail.com"
        user.save()

    def test_user_reset_password_form_valid(self):
        form_data = {'email': self.email_invalid_1}
        form = ResetPasswordForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_reset_password_form_invalid(self):
        form_data = {'email': self.email_valid_reset}
        form = ResetPasswordForm(data=form_data)
        self.assertTrue(form.is_valid())
