from django.test import TestCase
from user.forms import PatientForm
from user.models import User


class TestPatientForm(TestCase):
    def setUp(self):
        self.name_valid = 'Teste Nome'
        self.name_invalid = 'a12'
        self.name_invalid_TYPE = 'a@hjasgdjasd1al'
        self.name_invalid_MAX = 'aasdkgasghdhjadjasvdashdjavcdbnmhasdvbdmmasbdnmhamsjdhgegdhjgsavdhabvdbnasd'
        self.name_invalid_MIN = 'a'

        self.phone_valid = '1234567890'
        self.phone_invalid = '456'
        self.phone_invalid_MIN = '456'
        self.phone_invalid_TYPE = 'asdaaaaaads'
        self.phone_invalid_MAX = '456134564898761'

        self.email_valid = 'admin@admin.com'
        self.email_invalid = 'admin.com'
        self.email_invalid_TYPE = 'admin.com'
        self.email_invalid_MIN = 'a@a.a'
        self.email_invalid_MAX = 'admin@fgdhafdgfashgdfaghfdasfdghashjasghjasgdhjgasdjasjdjaasdsdfjh.com'
        self.email_invalid_BASE = 'admin@hotmail.com'

        self.password_valid = '1234567'
        self.password_invalid = '123456789'
        self.password_invalid_MAX = '1234567891011'
        self.password_invalid_MIN = '123'
        self.password_invalid_TYPE = 'a@d123a'

        self.date_of_birth_valid = '10/12/1990'
        self.date_of_birth_invalid = '18'
        self.date_of_birth_invalid_FORMAT = '18'
        self.date_of_birth_invalid_MIN = '10/12/2020'

        self.sex_valid = 'M'
        self.sex_invalid = 'A'

        self.id_document_valid = '12345678910654'
        self.id_document_invalid = '1'
        self.id_document_invalid_MIN = '1'
        self.id_document_invalid_MAX = '123456789101112131415161718192021222324252627282930'
        self.id_document_invalid_TYPE = '252627282930asdf'

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

    def test_forms_patient_name_is_not_valid_TYPE(self):
        form_data = {'name': self.name_invalid_TYPE,
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

    def test_forms_patient_name_is_not_valid_MIN(self):
        form_data = {'name': self.name_invalid_MIN,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_phone_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid_TYPE,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_phone_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid_MAX,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_phone_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid_MIN,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_email_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid_TYPE,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_email_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid_MAX,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_email_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid_MIN,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_email_is_not_valid_BASE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid_BASE,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_password_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid_TYPE,
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

    def test_forms_patient_password_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid_MAX,
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
                     'password': self.password_invalid_MAX,
                     'confirm_password': self.password_invalid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_id_document_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_invalid_TYPE,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_id_document_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_invalid_MIN,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_id_document_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_invalid_MAX,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_date_of_birth_is_not_valid_FORMAT(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_invalid_FORMAT}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_date_of_birth_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_invalid_MIN}
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

    def test_forms_patient_invalid_0(self):
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

    def test_forms_patient_invalid_1(self):
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

    def test_forms_patient_invalid_2(self):
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

    def test_forms_patient_invalid_3(self):
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

    def test_forms_patient_invalid_4(self):
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

    def test_forms_patient_invalid_5(self):
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

    def test_forms_patient_invalid_6(self):
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

    def test_forms_patient_invalid_7(self):
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

    def test_forms_patient_invalid_8(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid,
                     'email': self.email_invalid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_invalid_9(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid,
                     'email': self.email_valid,
                     'password': self.password_invalid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_invalid_10(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_invalid,
                     'id_document': self.id_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_invalid_11(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_invalid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'id_document': self.id_document_invalid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_forms_patient_invalid_12(self):
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
