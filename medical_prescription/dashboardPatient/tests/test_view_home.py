# django
from django.test import TestCase
from django.test.client import RequestFactory
from django.test.client import Client
from django.core.exceptions import PermissionDenied

# local django.
from dashboardPatient.views import HomePatient
from user.models import Patient


class TestRequestHomePatient(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.patient = Patient.objects.create_user(email='doctor@doctor.com',
                                                   password='senha12')

    def test_prescription_request_home_patient(self):
        request = self.factory.get('/dashboard_patient/patient')
        request.user = self.patient
        response = HomePatient.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_prescription_request_home_health_professional_fail(self):
        request = self.factory.get('/dashboard_patient/patient')
        request.user = Patient(email="email@email.com", password="password")

        with self.assertRaises(PermissionDenied):
            HomePatient.as_view()(request)
