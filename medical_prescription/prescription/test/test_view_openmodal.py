from django.test import TestCase
from django.test.client import RequestFactory, Client

from prescription.views import OpenPrescriptionView


class TestOpenModal(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.view = OpenPrescriptionView()

    def test_prescription_get(self):
        request = self.factory.get('/prescription')
        response = self.view.get(request)
        self.assertEqual(response.status_code, 200)
