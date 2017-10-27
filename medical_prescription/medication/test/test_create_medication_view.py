# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser

# Local Django imports
from medication.views import CreateMedicationView
from user.models import User, Patient, HealthProfessional


class CreateMedicationViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com', password='senha12')
        self.patient = Patient.objects.create_user(email='patient@patient.com', password='senha12')
        self.user = User.objects.create_user(email='user@user.com', password='senha12')

    def test_get_without_login(self):
        request = self.factory.get('/medication/create_medication/')
        request.user = AnonymousUser()

        response = CreateMedicationView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_get_with_patient(self):
        request = self.factory.get('/medication/create_medication/')
        request.user = self.patient

        response = CreateMedicationView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_get_with_health_professional(self):
        request = self.factory.get('/medication/create_medication/')
        request.user = self.health_professional

        response = CreateMedicationView.as_view()(request)
        self.assertEqual(response.status_code, 200)
