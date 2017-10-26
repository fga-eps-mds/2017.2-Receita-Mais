# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser


# Local Django imports
from user.models import Patient, HealthProfessional
from medication.models import Medication
from medication.views import UpdateMedication


class TesteEdit(TestCase):

    def setUp(self):
        self.model = Medication
        self.view = UpdateMedication()

    def teste_get_url_sucess(self):
        self.assertEqual(self.view.get_success_url(), '/medication/list_medication/')

    def teste_get_url_false(self):
        self.assertNotEqual(self.view.get_success_url(), 'error')


class UpdateMedicationTest(TestCase):
    """
    Testing methods of Class UpdateMedication.
    """
    def setUp(self):
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com', password='senha12')
        self.patient = Patient.objects.create_user(email='patient@patient.com', password='senha12')

        self.description = "Examina alguma coisa"
        self.name = "Alguma coisa"

        medication = Medication()
        medication.name = "Invalido"
        medication.description = "Alguma descricao"
        medication.active_ingredient = "qualquercoisa"
        medication.laboratory = "laboratorio"
        medication.health_professional = self.health_professional
        medication.pk = 1
        medication.save()

    # Testing view calls
    def test_get_without_login(self):
        request = self.factory.get('medication/edit_medication/(?P<pk>[0-9]+)/')
        request.user = AnonymousUser()

        response = UpdateMedication.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)

    def test_get_with_patient(self):
        request = self.factory.get('medication/edit_medication/(?P<pk>[0-9]+)/')
        request.user = self.patient

        response = UpdateMedication.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)

    def test_get_with_health_professional(self):
        request = self.factory.get('medication/edit_medication/(?P<pk>[0-9]+)/')
        request.user = self.health_professional

        response = UpdateMedication.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post_without_login(self):
        request = self.factory.post('medication/edit_medication/(?P<pk>[0-9]+)/',
                                    {'name': self.name,
                                     'description': self.description})
        request.user = AnonymousUser()

        response = UpdateMedication.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)

    def test_post_with_patient(self):
        request = self.factory.post('medication/edit_medication/(?P<pk>[0-9]+)/',
                                    {'name': self.name,
                                     'description': self.description})
        request.user = self.patient

        response = UpdateMedication.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)

    def test_post_with_health_professional(self):
        request = self.factory.post('medication/edit_medication/(?P<pk>[0-9]+)/',
                                    {'name': self.name,
                                     'description': self.description})
        request.user = self.health_professional

        response = UpdateMedication.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)
