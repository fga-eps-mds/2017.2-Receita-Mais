from django.test import TestCase

from user.models import User
from user.forms import UpdateUserForm


class TestUpdateUserForm(TestCase):

    def setUp(self):
        self.name_valid = 'Teste Nome'
        self.name_invalid = 'a a'
        self.name_invalid_MAX = 'hagdkagskasgdhjashjdgashjdghjgdsjasgdhjasgdhjgdhjagsdhjgasdhjgashjdgashjdgashjdg'
        self.name_invalid_MIN = 'a'

        self.date_of_birth_valid = '10/12/1990'
        self.date_of_birth_invalid = '18'
        self.date_of_birth_invalid_MIN = '10/12/2022'

        self.phone_valid = '(61)1234-56789'
        self.phone_invalid = 'a12345678'
        self.phone_invalid_MAX = '12345678912312310111212345612345678'
        self.phone_invalid_MIN = '12345'
        self.phone_invalid_TYPE = '1a!2#4*'

        self.email_valid_reset = 'admin@gmail.com'
        self.email_valid = 'admin@admin.com'
        self.email_invalid = 'admin.com'
        self.email_invalid_1 = 'admin@hotmail.com'

        self.sex_valid = 'M'
        self.sex_invalid = 'A'

        self.id_document_valid = '12345678910'
        self.id_document_invalid = '1234'

        self.password_valid = '1234567'
        self.password_invalid_MIN = '123'
        self.password_invalid = '1234567891011'
        self.password_invalid_MAX = '1234567891011'

        self.user = User()
        self.user.name = self.name_valid
        self.user.date_of_birth = "1990-12-10"
        self.user.phone = self.phone_valid
        self.user.sex = self.sex_valid
        self.user.set_password(self.password_valid)
        self.user.email = "admin@hotmail.com"
        self.user.save()

    def test_user_update_user_form_valid(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_user_update_user_form_name_is_not_valid(self):
        form_data = {'name': self.name_invalid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid}
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_user_update_user_form_name_is_not_valid_MAX(self):
        form_data = {'name': self.name_invalid_MAX,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_user_update_user_form_name_is_not_valid_MIN(self):
        form_data = {'name': self.name_invalid_MIN,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_user_update_user_form_date_of_birth_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_user_update_user_form_date_of_birth_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_invalid_MIN,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_user_update_user_form_phone_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid,
                     'sex': self.sex_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_user_update_user_form_phone_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid_MIN,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_user_update_user_form_phone_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid_MAX,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_user_update_user_form_phone_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid_TYPE,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_user_update_user_form_sex_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_invalid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

