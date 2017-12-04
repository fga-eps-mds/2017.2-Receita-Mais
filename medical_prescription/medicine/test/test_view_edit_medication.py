# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied

# Local Django imports
from user.models import Patient, HealthProfessional
from medicine.models import (Medicine,
                             ManipulatedMedicine)
from medicine.views import UpdateMedicine


class TestEdit(TestCase):

    def setUp(self):
        self.model = Medicine
        self.view = UpdateMedicine()

    def test_get_url_sucess(self):
        self.assertEqual(self.view.get_success_url(), '/pt-br/medicine/list_all_medicines/')

    def test_get_url_false(self):
        self.assertNotEqual(self.view.get_success_url(), 'error')


class UpdateMedicationTest(TestCase):
    """
    Testing methods of Class UpdateMedication.
    """
    def setUp(self):
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com', password='senha12')
        self.patient = Patient.objects.create_user(email='patient@patient.com',
                                                   password='senha12',
                                                   CEP='72850735',
                                                   UF='DF',
                                                   city='Brasília',
                                                   neighborhood='Asa sul',
                                                   complement='Bloco 2 QD 701')
        self.recipe_name = "Examina alguma coisa"
        self.composition = "Alguma coisa"

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
        self.manipulated_medicine.pk = 1
        self.manipulated_medicine.save()

    # Testing view calls
    def test_medicine_get_without_login(self):
        request = self.factory.get('medicine/edit_medicine/(?P<pk>[0-9]+)/')
        request.user = AnonymousUser()

        response = UpdateMedicine.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)

    def test_medicine_get_with_patient(self):
        request = self.factory.get('medicine/edit_medicine/(?P<pk>[0-9]+)/')
        request.user = self.patient

        with self.assertRaises(PermissionDenied):
            UpdateMedicine.as_view()(request, pk=1)

    def test_medicine_get_with_health_professional(self):
        request = self.factory.get('medicine/edit_medicine/(?P<pk>[0-9]+)/')
        request.user = self.health_professional

        response = UpdateMedicine.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_medicine_post_without_login(self):
        request = self.factory.post('medicine/edit_medicine/(?P<pk>[0-9]+)/',
                                    {'recipe_name': self.recipe_name,
                                     'composition': self.composition})
        request.user = AnonymousUser()

        response = UpdateMedicine.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)

    def test_medicine_post_with_patient(self):
        request = self.factory.post('medicine/edit_medicine/(?P<pk>[0-9]+)/',
                                    {'recipe_name': self.recipe_name,
                                     'composition': self.composition})
        request.user = self.patient

        with self.assertRaises(PermissionDenied):
            UpdateMedicine.as_view()(request, pk=1)

    def test_medicine_post_with_health_professional(self):
        request = self.factory.post('medicine/edit_medicine/(?P<pk>[0-9]+)/',
                                    {'recipe_name': self.recipe_name,
                                     'composition': self.composition})
        request.user = self.health_professional

        response = UpdateMedicine.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)
