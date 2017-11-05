# django
from django.test import TestCase
from django.test.client import RequestFactory
from django.http import HttpResponse
from django.test.client import Client

# local djngo.
from prescription.views import AutoCompleteCid
from user.models import HealthProfessional
from disease.models import Disease


class TestRequiredAutocompleteCid(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com',
                                                                          password='senha12')
        self.id_cid_10 = 'A00'
        self.description = 'A00	Cólera devida a Vibrio cholerae 01, biótipo cholerae'
        self.disease = Disease(id_cid_10=self.id_cid_10, description=self.description)
        self.disease.save()

    def test_prescription_request_autocomplete_cid_fail(self):
        request = self.factory.get('/prescription/ajax/autocomplete_cid/?term=A00')
        request.user = self.health_professional
        response = AutoCompleteCid.as_view()(request)
        self.assertNotEquals(response, HttpResponse)

    def test_prescription_request_autocomplete_cid_return_no_disease(self):
        request = self.factory.get('/prescription/ajax/autocomplete_cid/?term=test',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.health_professional
        response = AutoCompleteCid.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_prescription_request_autocomplete_cid_return_one_disease(self):
        request = self.factory.get('/prescription/ajax/autocomplete_cid/?term=A00',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.health_professional
        response = AutoCompleteCid.as_view()(request)
        self.assertEquals(response.status_code, 200)
