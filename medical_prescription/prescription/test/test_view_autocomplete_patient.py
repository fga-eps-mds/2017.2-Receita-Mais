# django
from django.test import TestCase
from django.test.client import RequestFactory
from django.http import HttpResponse
from django.test.client import Client

# local djngo.
from prescription.views import AutoCompletePatient
from user.models import (HealthProfessional,
                         Patient)


class TestRequiredAutocompletePatient(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com',
                                                                          password='senha12')
        self.patient = Patient.objects.create_user(name='Patient',
                                                   email='patient@patient.com',
                                                   password='senha12',
                                                   CEP='72850735',
                                                   UF='DF',
                                                   city='Brasília',
                                                   neighborhood='Asa sul',
                                                   complement='Bloco 2 QD 701')

    def test_prescription_request_autocomplete_patient_fail(self):
        request = self.factory.get('/prescription/ajax/autocomplete_patient/?term=Pat')
        request.user = self.health_professional
        response = AutoCompletePatient.as_view()(request)
        self.assertNotEquals(response, HttpResponse)

    def test_prescription_request_autocomplete_patient_return_no_patient(self):
        request = self.factory.get('/prescription/ajax/autocomplete_patient/?term=test',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.health_professional
        response = AutoCompletePatient.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_prescription_request_autocomplete_patient_return_one_patient(self):
        request = self.factory.get('/prescription/ajax/autocomplete_patient/?term=Pat',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.health_professional
        response = AutoCompletePatient.as_view()(request)
        self.assertEquals(response.status_code, 200)
