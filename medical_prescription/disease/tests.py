# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser

# Local Django imports
from .views import ListDisease
from user.views import LoginView
from user.models import User, Patient, HealthProfessional


class ListDiseaseViewTest(TestCase):
    def setUp(self):
        # Creating user in database.
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com', password='senha12')
        self.patient = Patient.objects.create_user(email='patient@patient.com',
                                                   password='senha12',
                                                   CEP='72850735',
                                                   UF='DF',
                                                   city='Brasília',
                                                   neighborhood='Asa sul',
                                                   complement='Bloco 2 QD 701')
        self.user = User.objects.create_user(email='user@user.com', password='senha12')

    def test_get_disease_without_login(self):
        request = self.factory.get('/disease/list_disease/')
        request.user = AnonymousUser()

        response = ListDisease.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_get_disease_with_patient(self):
        request = self.factory.get('/disease/list_disease/')
        request.user = self.patient

        response = ListDisease.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_get_disease_with_user(self):
        request = self.factory.get('/disease/list_disease/')
        request.user = self.user

        response = ListDisease.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_get_disease_with_health_professional(self):
        request = self.factory.get('/disease/list_disease/')
        request.user = self.health_professional

        response = ListDisease.as_view()(request)
        self.assertEqual(response.status_code, 200)
