# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied

# Local Django imports
from user.views import UpdateHealthProfessional
from user.models import User, Patient, HealthProfessional


class UpdateHealthProfessionalTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com',
                                                                          password='senha12', pk=99)

        self.patient = Patient.objects.create_user(email='patient@patient.com',
                                                   password='senha12',
                                                   CEP='72850735',
                                                   UF='DF',
                                                   city='Brasília',
                                                   neighborhood='Asa sul',
                                                   complement='Bloco 2 QD 701')

        self.user = User.objects.create_user(email='user@user.com',
                                             password='senha12')


    def test_user_edit_health_professional_with_patient(self):
        request = self.factory.get('user/edit_health_professional/(?P<pk>[0-9]+)/')
        request.user = self.patient

        with self.assertRaises(PermissionDenied):
            UpdateHealthProfessional.as_view()(request, pk=99)

    def test_user_edit_health_professional_with_user(self):
        request = self.factory.get('user/edit_health_professional/(?P<pk>[0-9]+)/')
        request.user = self.user

        with self.assertRaises(PermissionDenied):
            UpdateHealthProfessional.as_view()(request, pk=99)

    def test_user_edit_health_professional_with_own_health_professional(self):
        request = self.factory.get('user/edit_health_professional/(?P<pk>[0-9]+)/')
        request.user = self.health_professional

        response = UpdateHealthProfessional.as_view()(request, pk=99)
        self.assertEqual(response.status_code, 200)

    def test_user_edit_health_professional_with_health_professional(self):
        request = self.factory.get('user/edit_health_professional/(?P<pk>[0-9]+)/')
        request.user = self.health_professional

        with self.assertRaises(PermissionDenied):
            UpdateHealthProfessional.as_view()(request, pk=98)
