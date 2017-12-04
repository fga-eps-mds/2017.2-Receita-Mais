# Django
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied

from medicine.models import ActivePrinciple
from user.models import User, Patient, HealthProfessional
from medicine.views import ListAllPrinciple


class ListActivePrincipleViewTest(TestCase):
    def setUp(self):
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

    def test_medicine_get_without_login(self):
        request = self.factory.get('/medicine/list/')
        request.user = AnonymousUser()

        response = ListAllPrinciple.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_medicine_get_with_patient(self):
        request = self.factory.get('/medicine/list/')
        request.user = self.patient

        with self.assertRaises(PermissionDenied):
            ListAllPrinciple.as_view()(request)

    def test_medicine_get_with_health_professional(self):
        request = self.factory.get('/medicine/list/')
        request.user = self.health_professional

        response = ListAllPrinciple.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_medicine_active_principle_str(self):
        principle = ActivePrinciple()
        principle.name = 'Dipirona'
        test_str = str(principle)
        self.assertEquals(test_str, 'Dipirona')
