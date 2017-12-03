# django
from django.test import TestCase
from django.test.client import RequestFactory
from django.test.client import Client

# local djngo.
from dashboardHealthProfessional.views import HomeHealthProfessional
from user.models import HealthProfessional


class TestRequestHomeHealthProfessional(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com',
                                                                          password='senha12')

    def test_prescription_request_home_health_professional_fail(self):
        request = self.factory.get('/dashboard_health_professional/health_professional')
        request.user = HealthProfessional(email="email@email.com", password="password")
        response = HomeHealthProfessional.as_view()(request)
        self.assertEquals(response.status_code, 302)

    def test_prescription_request_home_health_professional(self):
        request = self.factory.get('/dashboard_health_professional/health_professional')
        request.user = self.health_professional
        response = HomeHealthProfessional.as_view()(request)
        self.assertEquals(response.status_code, 200)
