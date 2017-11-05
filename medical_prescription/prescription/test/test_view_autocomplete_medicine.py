# django
from django.test import TestCase
from django.test.client import RequestFactory
from django.http import HttpResponse
from django.test.client import Client

# local djngo.
from prescription.views import AutoCompleteMedicine
from user.models import HealthProfessional
from medicine.models import (Medicine,
                             ManipulatedMedicine)


class TestRequiredAutocompleteMedicine(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com',
                                                                          password='senha12')
        self.medicine = Medicine()
        self.medicine.name = "Medicamento Teste"
        self.medicine.active_ingredient = "Teste Lab"
        self.medicine.save()

        self.manipulated_medicine = ManipulatedMedicine()
        self.manipulated_medicine.recipe_name = "Manipulated Medicine"
        self.manipulated_medicine.physical_form = "Physical Form"
        self.manipulated_medicine.quantity = 10
        self.manipulated_medicine.measurement = 'kg'
        self.manipulated_medicine.composition = ("Manipulated Medicine Composition." +
                                                 "Manipulated Medicine Composition." +
                                                 "Manipulated Medicine Composition." +
                                                 "Manipulated Medicine Composition." +
                                                 "Manipulated Medicine Composition." +
                                                 "Manipulated Medicine Composition.")

        self.manipulated_medicine.health_professional = self.health_professional
        self.manipulated_medicine.save()

    def test_prescription_request_autocomplete_medicine_fail(self):
        request = self.factory.get('/prescription/ajax/autocomplete_medicine/?term=Med')
        request.user = self.health_professional
        response = AutoCompleteMedicine.as_view()(request)
        self.assertNotEquals(response, HttpResponse)

    def test_prescription_request_autocomplete_medicine_return_no_medicine(self):
        request = self.factory.get('/prescription/ajax/autocomplete_medicine/?term=testan',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.health_professional
        response = AutoCompleteMedicine.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_prescription_request_autocomplete_medicine_return_one_medicine(self):
        request = self.factory.get('/prescription/ajax/autocomplete_medicine/?term=Med',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.health_professional
        response = AutoCompleteMedicine.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_prescription_request_autocomplete_medicine_return_one_manipulatede_medicine(self):
        request = self.factory.get('/prescription/ajax/autocomplete_medicine/?term=Man',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.health_professional
        response = AutoCompleteMedicine.as_view()(request)
        self.assertEquals(response.status_code, 200)
