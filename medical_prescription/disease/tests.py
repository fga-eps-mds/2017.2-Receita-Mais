# Django imports
from django.test import TestCase
from django.test.client import RequestFactory, Client

# Local Django imports
from user.views import LoginView
from user.models import Patient, User, HealthProfessional


class ListDiseaseViewTest(TestCase):
    def setUp(self):
        # Creating user in database.
        self.user = HealthProfessional()
        user = User.objects.create(email='teste@teste.com')
        user.set_password('111555999')
        self.user.is_active = True
        self.user.save()

        self.factory = RequestFactory()
        self.login_view = LoginView()
        self.client = Client()

    def test_get_disease_without_login(self):
        # Test if get request of disease list without login is redirect to landing page.
        self.resp = self.client.get('/disease/list_disease/')
        self.assertRedirects(self.resp, '/?next=/disease/list_disease/')

'''
    def test_get_disease_with_patient(self):
        # Test if get request of disease list with patient is redirect to login health professional page.
        self.client.login(email='teste@teste.com', password='111555999')
        self.resp = self.client.get('/disease/list_disease/')
        self.assertRedirects(self.resp, '/user/login_healthprofessional/')
'''
