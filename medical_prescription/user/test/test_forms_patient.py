from django.test import TestCase

from user.models import User
from user.forms import PatientForm


class TestPatientForm(TestCase):

    def setUp(self):
        self.name_valid = 'Teste Nome'
        self.name_invalid = 'a'
        self.name_invalid_MAX = 'aasjdhghjasgdhjasfdhjasjdlaskldhkdhklasdhjadgadhjhkjdjkadhlaskjdghladg'

        self.date_of_birth_valid = '10/12/1990'
        self.date_of_birth_invalid = '18'

        self.phone_valid = '123456789'
        self.phone_invalid = '123456789101112'

        self.email_valid_reset = 'admin@gmail.com'
        self.email_valid = 'admin@admin.com'
        self.email_invalid = 'admin.com'
        self.email_invalid_1 = 'admin@hotmail.com'
        self.email_invalid_2 = 'adasdasdasdasasdadasdaddmin@hoasdasdasdasdasdasdasdasdasdasdasdtmail.com'

        self.sex_valid = 'M'
        self.sex_invalid = 'A'

        self.crm_valid = '12345'
        self.crm_invalid = '1'

        self.crm_state_valid = 'DF'
        self.crm_state_invalid = 'a'

        self.id_document_valid = '12345678910'
        self.id_document_invalid = '1'

        self.password_valid = '1234567'
        self.password_invalid = '1234567891011'
        self.password_invalid_MIN = '123'
        self.password_invalid_MAX = '73512356123123612376125312e351235612531263512635e561265368126536712837'

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
                     'date_of_birth': self.date_of_birth_valid,
                     'id_document_state': 'DF'}
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

    def test_forms_patient_name_is_not_valid_MAX(self):
        form_data = {'name': self.name_invalid_MAX,
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

    def test_forms_patient_email_is_not_valid2(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid_2,
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

    def test_forms_patient_password_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid_MIN,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_password_confirmation_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid_MAX,
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
