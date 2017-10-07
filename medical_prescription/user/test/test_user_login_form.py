from django.test import TestCase

from user.models import User
from user.forms import UserLoginForm


class TestUserForm(TestCase):

    def setUp(self):
        self.email_valid_reset = 'admin@gmail.com'
        self.email_valid = 'admin@admin.com'
        self.email_invalid = 'admin.com'
        self.email_invalid_1 = 'admin@hotmail.com'
        self.email_invalid_NULL = None

        self.password_valid = '1234567'
        self.password_invalid = '1234567891011'
        self.password_invalid_NULL = None

        user = User()
        user.email = "admin@hotmail.com"
        user.save()

        user1 = User()
        user1.email = "admin@admin.com"
        user1.is_active = False
        user1.save()

    def test_user_login_form_valid(self):
        form_data = {'email': self.email_valid,
                     'password': self.password_valid}
        form = UserLoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_login_form_invalid(self):
        form_data = {'email': self.email_invalid,
                     'password': self.password_invalid}
        form = UserLoginForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_login_form_invalid_all(self):
        form_data = {'email': self.email_invalid,
                     'password': self.password_invalid}
        form = UserLoginForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_login_form_invalid_NULL_0(self):
        form_data = {'email': self.email_invalid_NULL,
                     'password': self.password_invalid}
        form = UserLoginForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_login_form_invalid_NULL_1(self):
        form_data = {'email': self.email_invalid,
                     'password': self.password_invalid_NULL}
        form = UserLoginForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_login_form_invalid_NULL_2(self):
        form_data = {'email': self.email_invalid,
                     'password': self.password_invalid_NULL}
        form = UserLoginForm(data=form_data)
        self.assertFalse(form.is_valid())
