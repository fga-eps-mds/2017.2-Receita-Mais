from django.test import TestCase
from django.test.client import RequestFactory, Client

from user.views import RegisterPatientView


class RegisterPatientViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.my_view = RegisterPatientView()
        self.client = Client()
        self.name_valid = 'Teste Nome'
        self.date_of_birth_valid = '10/12/1990'
        self.phone_valid = '123456789'
        self.email_valid = 'admin@admin.com'
        self.sex_valid = 'M'
        self.crm_valid = '12345'
        self.crm_state_valid = 'DF'
        self.id_document_valid = '12345678910'
        self.password_valid = '1234567'

    def test_get(self):
        request = self.factory.get('user/register_patient/')
        response = self.my_view.get(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        context = {'name': self.name_valid,
                   'phone': self.phone_valid,
                   'email': self.email_valid,
                   'password': self.password_valid,
                   'confirm_password': self.password_valid,
                   'crm': self.crm_valid,
                   'crm_state': self.crm_state_valid,
                   'sex': self.sex_valid,
                   'date_of_birth': self.date_of_birth_valid}

        response = self.client.post('/user/register_health_professional/', context)

        # If the method redirect correctly the status code 200 is returned.
        self.assertEqual(response.status_code, 200)
