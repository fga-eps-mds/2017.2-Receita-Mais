# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
# Local django imports
from user.views import ListLinkedPatientsView
from user.models import HealthProfessional


class TestListLinkedPatients(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com', password='senha12')

    def test_user_user_get_exam_with_health_professional(self):
        request = self.factory.get('/user/listlinkedpatients')
        request.user = self.health_professional

        response = ListLinkedPatientsView.as_view()(request)
        self.assertEqual(response.status_code, 200)
