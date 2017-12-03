from django.test import TestCase

from user.models import HealthProfessional, User
from user.forms import HealthProfessionalForm


class TestHealthProfessionalForm(TestCase):

    def setUp(self):
        self.name_valid = 'Teste Nome'
        self.name_invalid = 'T'
        self.name_invalid_TYPE = 'a@hjasgdjasda1l'
        self.name_invalid_MAX = 'aasdkgasghdhjadjasvdashdjavcdbnmhasdvbdmmasbdnmhamsjdhgegdhjgsavdhabvdbnasd'
        self.name_invalid_MIN = 'a'

        self.phone_valid = '(61)1234-56789'
        self.phone_invalid = '456'
        self.phone_invalid_MIN = '456'
        self.phone_invalid_TYPE = 'aas1@a;$aaa'
        self.phone_invalid_MAX = '456134564898761'

        self.email_valid = 'admin@admin.com'
        self.email_invalid = 'admin.com'
        self.email_invalid_TYPE = 'admin.com'
        self.email_invalid_MIN = 'a@a.'
        self.email_invalid_MAX = 'admin@fgdhafdgfashgdfaghfdasfdghashjasghjasgdhjgasdjasjdjaasdsdfjh.com'
        self.email_invalid_BASE = 'admin@hotmail.com'

        self.password_valid = '1234567'
        self.password_invalid = '123'
        self.password_invalid_MAX = '1234567891011'
        self.password_invalid_MIN = '123'
        self.password_invalid_TYPE = 'a@d13!*'

        self.date_of_birth_valid = '10/12/1990'
        self.date_of_birth_invalid = '18'
        self.date_of_birth_invalid_FORMAT = '18'
        self.date_of_birth_invalid_MIN = '10/12/2010'

        self.sex_valid = 'M'
        self.sex_invalid = 'A'

        self.crm_valid = '12345'
        self.crm_valid_existent = '54321'
        self.crm_invalid = '1'
        self.crm_invalid_MIN = '13'
        self.crm_invalid_MAX = '1564564564689756431367'
        self.crm_invalid_FORMAT = 'a4'
        self.crm_invalid_TYPE = 'a1@13'

        self.crm_state_valid = 'DF'
        self.crm_state_invalid = '1234a'
        self.crm_state_invalid_MAX = 'aaaaaaaa'
        self.crm_state_invalid_MIN = 'A'
        self.crm_state_invalid_NONE = None

        self.speciality_valid = 'Alergia'
        self.speciality_invalid_MIN = 'A'
        self.speciality_invalid_MAX = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

        user = HealthProfessional()
        user.crm = "54321"
        user.save()

        user = User()
        user.email = "admin@hotmail.com"
        user.save()

    def test_user_forms_health_professional_is_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_forms_health_professional_name_is_not_valid(self):
        form_data = {'name': self.name_invalid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_name_is_not_valid_MAX(self):
        form_data = {'name': self.name_invalid_MAX,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_name_is_not_valid_MIN(self):
        form_data = {'name': self.name_invalid_MIN,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_name_is_not_valid_TYPE(self):
        form_data = {'name': self.name_invalid_TYPE,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_phone_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid_MIN,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_valid,
                     'crm': self.crm_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_phone_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid_TYPE,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_valid,
                     'crm': self.crm_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_phone_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_invalid_MAX,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'password_confirmation': self.password_valid,
                     'crm': self.crm_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_email_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid_TYPE,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_email_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid_MAX,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_email_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid_MIN,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_email_is_not_valid_BASE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_invalid_BASE,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_password_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid_MAX,
                     'confirm_password': self.password_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_password_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid_MIN,
                     'confirm_password': self.password_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_password_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid_TYPE,
                     'confirm_password': self.password_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_password_confirmation_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_invalid_MIN,
                     'crm': self.crm_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_password_confirmation_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_invalid_MIN,
                     'confirm_password': self.password_invalid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_crm_is_not_valid_FORMAT(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_invalid_FORMAT,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_crm_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_invalid_MAX,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_crm_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_invalid_MIN,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_crm_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_invalid_TYPE,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_crm_is_not_valid_existent(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid_existent,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_crm_state_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_invalid_MAX,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}

        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_crm_state_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_invalid_MIN,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}

        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_crm_state_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm_state': self.crm_state_invalid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}

        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_crm_state_is_not_valid_NONE(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm_state': self.crm_state_invalid_NONE,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_valid}

        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_sex_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_invalid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_date_of_birth_is_not_valid_FORMAT(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'date_of_birth': self.date_of_birth_invalid_FORMAT}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_date_of_birth_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_valid,
                     'date_of_birth': self.date_of_birth_invalid_MIN}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_specialty_first_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'specialty_first': self.speciality_invalid_MIN,
                     'specialty_second': self.speciality_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_specialty_first_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'specialty_first': self.speciality_invalid_MAX,
                     'specialty_second': self.speciality_valid,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_specialty_second_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_invalid_MIN,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_forms_health_professional_specialty_second_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'phone': self.phone_valid,
                     'email': self.email_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid,
                     'crm': self.crm_valid,
                     'crm_state': self.crm_state_valid,
                     'sex': self.sex_valid,
                     'specialty_first': self.speciality_valid,
                     'specialty_second': self.speciality_invalid_MAX,
                     'date_of_birth': self.date_of_birth_valid}
        form = HealthProfessionalForm(data=form_data)
        self.assertFalse(form.is_valid())
