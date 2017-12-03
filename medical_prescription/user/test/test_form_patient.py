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

        self.phone_valid = '(61)1234-56789'
        self.phone_invalid = '456'
        self.phone_invalid_MIN = '456'
        self.phone_invalid_TYPE = 'asdaaaaaads'
        self.phone_invalid_MAX = '456134564898761'

        self.email_valid = 'admin@admin.com'
        self.email_invalid = 'admin.com'
        self.email_invalid_TYPE = 'admin.com'
        self.email_invalid_MIN = 'a@a.a'
        self.email_invalid_MAX = 'admin@fgdhafdgfashgdfaghfdasfdghashjasghjasgdhjgasdjasjdjaasdsdfjh.com'

        self.password_valid = '1234567'
        self.password_invalid = '123456789'
        self.password_invalid_MAX = '1234567891011'
        self.password_invalid_MIN = '123'
        self.password_invalid_TYPE = 'a@d123!'

        self.date_of_birth_valid = '10/12/1990'
        self.date_of_birth_invalid = '18'
        self.date_of_birth_invalid_FORMAT = '18'
        self.date_of_birth_invalid_MIN = '10/12/2020'

        self.sex_valid = 'M'
        self.sex_invalid = 'A'

        self.CPF_document_valid = '61367541000'
        self.CPF_document_invalid = '11111111111'
        self.CPF_document_invalid_MIN = '111111111'
        self.CPF_document_invalid_MAX = '11111111111'
        self.CPF_document_invalid_TYPE = '252627282930asdf'
        self.CPF_document_invalid_NONE = None

        self.CEP_valid = 72850735
        self.CEP_invalid = '7285073A'
        self.CEP_invalid_MIN = 42
        self.CEP_invalid_MAX = 728507351

        self.UF_valid = 'DF'
        self.UF_invalid = ''
        self.UF_invalid_MIN = 'A'
        self.UF_invalid_MAX = 'AAA'

        self.city_valid = 'Brasília'
        self.city_invalid = ''
        self.city_invalid_MAX = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

        self.neighborhood_valid = 'Setor Leste'
        self.neighborhood_invalid = ''
        self.neighborhood_invalid_MAX = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

        self.complement_valid = 'Rua 01, Quadra 10, Lote 15'
        self.complement_invalid = ''
        self.complement_invalid_MAX = '''aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                                         aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                                         aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'''

        user = User()
        user.email = "admin@hotmail.com"
        user.save()

    def test_user_forms_patient_is_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_forms_patient_name_is_not_valid_TYPE(self):
        form_data = {'name': self.name_invalid_TYPE,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_name_is_not_valid_MAX(self):
        form_data = {'name': self.name_invalid_MAX,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_name_is_not_valid_MIN(self):
        form_data = {'name': self.name_invalid_MIN,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_phone_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid_TYPE,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_phone_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid_MAX,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_phone_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid_MIN,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_email_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid_TYPE,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_password_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid_TYPE,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_password_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid_MIN,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_password_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid_MAX,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_password_confirmation_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid_MAX,
                     'confirm_password': self.password_invalid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_CPF_document_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_invalid_TYPE,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_CPF_document_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_invalid_MIN,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_CPF_document_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_invalid_MAX,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_date_of_birth_is_not_valid_FORMAT(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_invalid_FORMAT,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_date_of_birth_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_invalid_MIN,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_sex_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_invalid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_CEP_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_invalid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_invalid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_CEP_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_invalid_MAX,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_UF_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_invalid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_UF_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_invalid_MAX,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_city_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_invalid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_city_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_invalid_MAX,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_neighborhood_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_invalid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_neighborhood_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_invalid_MAX,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_complement_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_invalid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_complement_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_invalid_MAX}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_patient_id_document_is_not_valid_NONE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'CPF_document': self.CPF_document_invalid_NONE,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'CEP': self.CEP_valid,
                     'UF': self.UF_valid,
                     'city': self.city_valid,
                     'neighborhood': self.neighborhood_valid,
                     'complement': self.complement_valid}
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())
