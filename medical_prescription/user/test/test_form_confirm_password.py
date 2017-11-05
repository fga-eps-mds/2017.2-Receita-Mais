from django.test import TestCase
from user.forms import ConfirmPasswordForm


class TesteConfirmPassworForm(TestCase):

    def setUp(self):
        self.form = ConfirmPasswordForm

    # Test if password and confirmpasswort is equal.
    def test_user_password_confirm_true(self):
        context = {'password': 'Teste12345', 'password_confirmation': 'Teste12345'}
        form = self.form(data=context)

        self.assertTrue(form.is_valid())

    def test_user_password_confirm_false(self):
        context = {'password': 'Teste12345', 'password_confirmation': 'Teste12445'}
        form = self.form(data=context)

        self.assertFalse(form.is_valid())
