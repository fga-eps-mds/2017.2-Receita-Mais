# Django imports
from django.test import TestCase

# Local Django imports
from user.forms import PatientForm


class TestPatientForm(TestCase):

    def setUp(self):
        self.form = PatientForm

        self.name_valid = 'Teste'
        self.name_invalid = '12345'
        self.name_invalid_MAX = 'testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
        self.name_invalid_MIN = 'a'

        self.email_valid = 'teste@teste.com'
        self.email_invalid = 'teste.com'
        self.email_invalid_TYPE = 'teste.com'
        self.email_invalid_MIN = 'a@a.'
        self.email_invalid_MAX = 'admin@fgdhafdgfashgdfaghfdasfdghashjasghjasgdhjgasdjafffffffffffffffffffffffffffj.com'

        self.phone_valid = '1234567890'
        self.phone_invalid = '123'
        self.phone_invalid_MIN = '1'
        self.phone_invalid_TYPE = 'aas1@a;$aaa'
        self.phone_invalid_MAX = '456134564898761'

        self.password_valid = '1234567'
        self.password_invalid = '123'
        self.password_invalid_MAX = '1234567891011'
        self.password_invalid_MIN = '123'
        self.password_invalid_TYPE = 'a@d13!*'

        self.date_of_birth_valid = '10/12/1990'
        self.date_of_birth_invalid = '18'
        self.date_of_birth_invalid_FORMAT = '18'

        self.id_document_valid = '93898393883'
        self.id_document_invalid = 'cpf'
        self.id_document_invalid_MIN = '1'
        self.id_document_invalid_MAX = '123456789123456789123456789123456789'

        self.sex_valid = 'M'
        self.sex_invalid = 'A'

    def test_forms_patient_is_valid(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = self.form(data=context)

        self.assertTrue(form.is_valid())

    def test_forms_patient_name_is_invalid(self):
        context = {'name': self.name_invalid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = self.form(data=context)

        self.assertFalse(form.is_valid())

    def test_forms_patient_name_is_invalid_MIN(self):
        context = {'name': self.name_invalid_MIN,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = self.form(data=context)

        self.assertFalse(form.is_valid())

    def test_forms_patient_name_is_invalid_MAX(self):
        context = {'name': self.name_invalid_MAX,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = self.form(data=context)

        self.assertFalse(form.is_valid())

    def test_forms_patient_email_is_invalid(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_invalid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = self.form(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_email_is_invalid_TYPE(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_invalid_TYPE,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = self.form(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_email_is_invalid_MAX(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_invalid_MAX,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = self.form(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_email_is_invalid_MIN(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_invalid_MIN,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = self.form(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_password_is_invalid(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_invalid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_password_is_invalid_type(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_invalid_TYPE,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_password_is_invalid_MIN(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_invalid_MIN,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_password_is_invalid_MAX(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_invalid_MAX,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_confirm_password_is_invalid(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_invalid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_confirm_password_is_invalid_type(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_invalid_TYPE,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_confirm_password_is_invalid_MIN(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_invalid_MIN,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_confirm_password_is_invalid_MAX(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_invalid_MAX,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_phone_is_invalid(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_invalid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_phone_is_invalid_type(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_invalid_TYPE,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_phone_is_invalid_MAX(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_invalid_MAX,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_phone_is_invalid_MIN(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_invalid_MIN,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_date_of_birth_is_invalid(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_invalid,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_date_of_birth_is_invalid_format(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_invalid_FORMAT,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_sex_is_invalid(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_invalid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_valid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_id_document_is_invalid(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_invalid}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_id_document_is_invalid_MIN(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_invalid_MIN}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())

    def test_forms_patient_id_document_is_invalid_MAX(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid,
                   'id_document': self.id_document_invalid_MAX}

        form = PatientForm(data=context)
        self.assertFalse(form.is_valid())
