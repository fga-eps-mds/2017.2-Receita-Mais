from django.test import TestCase
from django.test.client import RequestFactory, Client

from user.views import RegisterHealthProfessionalView


class RegisterHealthProfessionalViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.my_view = RegisterHealthProfessionalView()
        self.client = Client()

    # Testing method 'get' of HealthProfessionalView.
    def test_user_get(self):
        request = self.factory.get('user/register_health_professional/')
        response = self.my_view.get(request)
        self.assertEqual(response.status_code, 200)

    def test_user_post(self):
        context = {'email': 'test@test.com',
                   'password': '1st234567',
                   'confirm_password': '1st234567',
                   'name': 'Teste registro',
                   'sex': 'M',
                   'phone': '(61)1234-56789',
                   'date_of_birth': '10/12/1990',
                   'crm': '12347',
                   'specialty_first': 'Homeopatia',
                   'specialty_second': 'Homeopatia',
                   'crm_state': 'DF'}
        response = self.client.post('/user/register_health_professional/', context)

        # If the method redirect the status code 302 is returned.
        self.assertEqual(response.status_code, 302)

    def test_user_post_invalid(self):
        context = {'email': 'test@test.com',
                   'password': '1st234567',
                   'confirm_password': '1st234567',
                   'name': 'Teste registro',
                   'sex': 'A',
                   'phone': '6699999999',
                   'date_of_birth': '10/12/1990',
                   'specialty_first': 'Homeopatia',
                   'specialty_second': 'Homeopatia',
                   'crm': '12347',
                   'crm_state': 'DF'}
        response = self.client.post('/user/register_health_professional/', context)

        self.assertEqual(response.status_code, 200)
