# django
from django.test import TestCase
from django.test.client import RequestFactory
from django.http import HttpResponse
from django.test.client import Client

# local djngo.
from dashboardHealthProfessional.views import ChartData
from user.models import HealthProfessional


class TestRequiredChartData(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com',
                                                                          password='senha12')

    def test_prescription_request_chart_data_fail(self):
        request = self.factory.get('/dashboard_health_professional/ajax/chart_data')
        request.user = self.health_professional
        response = ChartData.as_view()(request)
        self.assertNotEquals(response, HttpResponse)

    def test_prescription_request_chart_data_return_no_data(self):
        request = self.factory.get('/dashboard_health_professional/ajax/chart_data',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.health_professional
        response = ChartData.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_prescription_request_chart_data_return_data(self):
        request = self.factory.get('/dashboard_health_professional/ajax/chart_data',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.health_professional
        response = ChartData.as_view()(request)
        self.assertEquals(response.status_code, 200)
