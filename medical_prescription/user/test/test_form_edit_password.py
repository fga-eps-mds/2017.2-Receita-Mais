from django.test import TestCase

from user.models import User
from user.forms import UpdatePasswordForm


class TestUpdateUserForm(TestCase):

    def setUp(self):
        self.old_password_valid = '1234567'
        self.old_password_invalid = '12345699'
        self.password_valid = '123456789'
        self.password_invalid_MIN = '123'
        self.password_invalid_MAX = '1234567891011'
        self.password_confirmation_invalid = '1234567890'

        self.user = User()
        self.user.name = 'Nome Valido'
        self.user.date_of_birth = "1990-12-10"
        self.user.phone = '61982224133'
        self.user.sex = 'M'
        self.user.set_password(self.old_password_valid)
        self.user.email = "admin@hotmail.com"
        self.user.save()

    def test_user_update_password_form_valid(self):
        form_data = {'old_password': self.old_password_valid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_valid
                     }
        form = UpdatePasswordForm(user=self.user, data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_update_password_form_old_invalid(self):
        form_data = {'old_password': self.old_password_invalid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_valid
                     }
        form = UpdatePasswordForm(user=self.user, data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_update_password_form_new_invalid(self):
        form_data = {'old_password': self.old_password_valid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_confirmation_invalid
                     }
        form = UpdatePasswordForm(user=self.user, data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_update_password_form_new_invalid_MIN(self):
        form_data = {'old_password': self.old_password_valid,
                     'password': self.password_invalid_MIN,
                     'password_confirmation': self.password_invalid_MIN
                     }
        form = UpdatePasswordForm(user=self.user, data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_update_password_form_new_invalid_MAX(self):
        form_data = {'old_password': self.old_password_valid,
                     'password': self.password_invalid_MAX,
                     'password_confirmation': self.password_invalid_MAX
                     }
        form = UpdatePasswordForm(user=self.user, data=form_data)
        self.assertFalse(form.is_valid())
