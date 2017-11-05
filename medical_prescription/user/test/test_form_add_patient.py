from django.test import TestCase
from user.forms import AddPatientForm


class TestAddPatientForm(TestCase):

    def setUp(self):
        self.form = AddPatientForm
        self.email_valid = 'teste@teste.com'
        self.email_invalid = 'teste.com'
        self.email_invalid_TYPE = 'teste.com'
        self.email_invalid_MIN = 'a@a.'
        self.email_invalid_MAX = 'teste@testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.com'

    def test_user_forms_add_patient_email_is_valid(self):
        context = {'email': self.email_valid}
        form = self.form(data=context)

        self.assertTrue(form.is_valid())

    def test_user_forms_add_patient_email_is_not_valid_TYPE(self):
        context = {'email': self.email_invalid_TYPE}

        form = self.form(data=context)
        self.assertFalse(form.is_valid())

    def test_user_forms_add_patient_email_is_not_valid_MAX(self):
        context = {'email': self.email_invalid_MAX}

        form = self.form(data=context)
        self.assertFalse(form.is_valid())

    def test_user_forms_add_patient_email_is_not_valid_MIN(self):
        context = {'email': self.email_invalid_MIN}

        form = self.form(data=context)
        self.assertFalse(form.is_valid())
