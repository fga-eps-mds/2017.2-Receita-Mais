from django.test import TestCase

from user.models import User
from user.forms import UpdateUserForm


class TestUpdateUserForm(TestCase):

    def setUp(self):
        self.name_valid = 'Teste Nome'
        self.name_invalid = 'a'
        self.name_invalid_MAX = 'hagdkagskasgdhjashjdgashjdghjgdsjasgdhjasgdhjgdhjagsdhjgasdhjgashjdgashjdgashjdg'
        self.name_invalid_MIN = 'a'

        self.date_of_birth_valid = '10/12/1990'
        self.date_of_birth_invalid = '18'
        self.date_of_birth_invalid_MIN = '10/12/2002'

        self.phone_valid = '123456789'
        self.phone_invalid = '12345678910111212345612345678'

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

        user = User()
        user.email = "admin@hotmail.com"
        user.save()

    def test_update_user_form_valid(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_update_user_form_name_is_not_valid(self):
        form_data = {'name': self.name_invalid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_name_is_not_valid_MAX(self):
        form_data = {'name': self.name_invalid_MAX,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_name_is_not_valid_MIN(self):
        form_data = {'name': self.name_invalid_MIN,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_date_of_birth_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_date_of_birth_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_invalid_MIN,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_phone_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_sex_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_invalid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_password_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_invalid_MAX,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_password_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_invalid_MIN,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid(self):
        form_data = {'name': self.name_invalid,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_invalid,
                     'sex': self.sex_invalid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_invalid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid1(self):
        form_data = {'name': self.name_invalid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid2(self):
        form_data = {'name': self.name_invalid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_invalid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid3(self):
        form_data = {'name': self.name_invalid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid4(self):
        form_data = {'name': self.name_invalid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_invalid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid5(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_invalid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid6(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_valid,
                     'sex': self.sex_invalid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid7(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid8(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_invalid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid9(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid,
                     'sex': self.sex_invalid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid10(self):
        form_data = {'name': self.name_invalid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid,
                     'sex': self.sex_valid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_invalid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid11(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_invalid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid12(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_invalid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid13(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_invalid,
                     'password': self.password_valid,
                     'confirm_password': self.password_invalid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid14(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_invalid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())
