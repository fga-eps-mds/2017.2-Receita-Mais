from django.test import TestCase

from user.models import User, HealthProfessional
from user.forms import PatientForm, HealthProfessionalForm, UserLoginForm
from user.forms import ResetPasswordForm, ConfirmPasswordForm, UpdateUserForm


class LoginTeste(TestCase):
    def setUp(self):
        self.user = User()
        self.user.name = "Felipe"
        self.user.date_of_birth = "1995-01-01"
        self.user.phone = "9999-9999"
        self.user.sex = "F"
        self.user.email = "user@user.com"
        self.user.password = "testando"
        self.user.save()

    def test_save_name(self):
        self.assertEqual(self.user.name, "Felipe")

    def test_save_date_of_birth(self):
        self.assertEqual(self.user.date_of_birth, "1995-01-01")

    def test_save_phone(self):
        self.assertEqual(self.user.phone, "9999-9999")

    def test_save_sex(self):
        self.assertEqual(self.user.sex, "F")

    def test_save_email(self):
        self.assertEqual(self.user.email, "user@user.com")

    def test_save_password(self):
        self.assertEqual(self.user.password, "testando")

    def test_get_short_name(self):
        user_name = User.objects.get(name="Felipe")
        self.assertEqual(user_name.get_short_name(), "Felipe")


class TestHealthProfessionalForm(TestCase):

    def setUp(self):
        self.name_valid = 'Teste Nome'
        self.name_invalid = 'a'

        self.date_of_birth_valid = '10/12/1990'
        self.date_of_birth_invalid = '18'

        self.phone_valid = '123456789'
        self.phone_invalid = '456'

        self.email_valid = 'admin@admin.com'
        self.email_invalid = 'admin.com'
        self.email_invalid_MAX = 'admin@fgdhafdgfashgdfaghfdasfdghashjasghjasgdhjgasdjasjdjaasdsdfjh.com'

        self.sex_valid = 'M'
        self.sex_invalid = 'A'

        self.crm_valid = '12345'
        self.crm_valid_existent = '54321'
        self.crm_invalid = '1'
        self.crm_invalid_format = ''

        self.crm_state_valid = 'DF'
        self.crm_state_invalid = 'a'
        self.crm_state_invalid_MAX = 'aaaaaaaa'

        self.id_document_valid = '12345678910'
        self.id_document_invalid = '1234'

        self.password_valid = '1234567'
        self.password_invalid = '1234567891011'

        user = HealthProfessional()
        user.crm = "54321"
        user.save()

    def test_forms_health_professional_is_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_forms_health_professional_name_is_not_valid(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_phone_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_email_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_email_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid_MAX,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_password_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_password_confirmation_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_invalid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_crm_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_invalid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_crm_is_not_valid_existent(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid_existent,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_crm_state_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_invalid_MAX,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}

        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_sex_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_invalid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_date_of_birth_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_invalid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_invalid,
                     'email': self.email_invalid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_invalid,
                     'crm': self.crm_invalid,
                     'crm_state': self.crm_state_invalid,
                     'sex': self.sex_invalid,
                     'date_of_birth': self.date_of_birth_invalid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid1(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_invalid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid2(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid3(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid4(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_invalid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid5(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_invalid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid6(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_invalid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid7(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_invalid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_health_professional_invalid8(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_invalid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())


class TestPatientForm(TestCase):

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
        self.crm_state_invalid = 'a'

        self.id_document_valid = '12345678910'
        self.id_document_invalid = '1234'

        self.password_valid = '1234567'
        self.password_invalid = '1234567891011'

        user = User()
        user.email = "admin@hotmail.com"
        user.save()

    def test_forms_patient_is_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_forms_patient_name_is_not_valid(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_phone_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_email_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_password_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_password_confirmation_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_invalid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_id_document_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_invalid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_date_of_birth_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_invalid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_sex_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_invalid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_invalid(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_invalid,
                     'email': self.email_invalid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_invalid,
                     'id_document': self.id_document_invalid,
                     'sex': self.sex_invalid,
                     'date_of_birth': self.date_of_birth_invalid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_invalid1(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_invalid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_invalid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_invalid2(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_invalid3(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_invalid4(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_invalid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_invalid5(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_invalid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_invalid6(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_invalid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_invalid7(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_invalid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())


class TestUserForm(TestCase):

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

    def test_reset_password_form_valid(self):
        form_data = {'email': self.email_invalid_1}
        form = ResetPasswordForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_reset_password_form_invalid(self):
        form_data = {'email': self.email_valid_reset}
        form = ResetPasswordForm(data=form_data)
        self.assertFalse(form.is_valid())


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

    def test_password_confirmation_form_valid(self):
        form_data = {'password': self.password_valid,
                     'password_confirmation': self.password_valid}
        form = ConfirmPasswordForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_password_confirmation_form_invalid_match(self):
        form_data = {'password': self.password_valid,
                     'password_confirmation': self.password_invalid_match}
        form = ConfirmPasswordForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_password_confirmation_form_invalid(self):
        form_data = {'password': self.password_invalid_MAX,
                     'password_confirmation': self.password_invalid_MIN}
        form = ConfirmPasswordForm(data=form_data)
        self.assertFalse(form.is_valid())


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
        self.phone_invalid = '123456789101112'

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
