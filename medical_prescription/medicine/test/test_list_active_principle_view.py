# Django
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser

from medicine.models import ActivePrinciple
from user.views import LoginView
from user.models import User, Patient, HealthProfessional
from medicine.views import ListActivePrinciple


class ListActivePrincipleViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com', password='senha12')
        self.patient = Patient.objects.create_user(email='patient@patient.com', password='senha12')
        self.user = User.objects.create_user(email='user@user.com', password='senha12')

    def test_get_without_login(self):
        request = self.factory.get('/medicine/list/')
        request.user = AnonymousUser()

        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_get_with_patient(self):
        request = self.factory.get('/medicine/list/')
        request.user = self.patient

        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_get_with_user(self):
        request = self.factory.get('/medicine/list/')
        request.user = self.user

        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_get_with_health_professional(self):
        request = self.factory.get('/medicine/list/')
        request.user = self.health_professional

        response = ListActivePrinciple.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_active_principle_str(self):
        principle = ActivePrinciple()
        principle.name = 'Dipirona'
        teste_str = str(principle)
        self.assertEquals(teste_str, 'Dipirona')
