# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied

# Local Django imports
from medicine.views import EditCustomActivePrinciple
from medicine.models import CustomActivePrinciple
from user.models import HealthProfessional, Patient


class EditCustomActivePrincipleTest(TestCase):
    """
    Testing methods of Class EditCustomActivePrinciple.
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
        self.description = "Examina alguma coisa"
        self.name = "Alguma coisa"

        custom_principle = CustomActivePrinciple()
        custom_principle.created_by = self.health_professional
        custom_principle.pk = 1
        custom_principle.save()

    # Testing view calls
    def test_medicine_get_without_login(self):
        request = self.factory.get('medicine/edit/(?P<pk>[0-9]+)/')
        request.user = AnonymousUser()

        response = EditCustomActivePrinciple.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)

    def test_medicine_get_with_patient(self):
        request = self.factory.get('medicine/edit/(?P<pk>[0-9]+)/')
        request.user = self.patient

        with self.assertRaises(PermissionDenied):
            EditCustomActivePrinciple.as_view()(request, pk=1)

    def test_medicine_get_with_health_professional(self):
        request = self.factory.get('medicine/edit/(?P<pk>[0-9]+)/')
        request.user = self.health_professional

        response = EditCustomActivePrinciple.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)

    # Testing post
    def test_medicine_post_without_login(self):
        request = self.factory.post('medicine/edit/(?P<pk>[0-9]+)/',
                                    {'name': self.name})
        request.user = AnonymousUser()

        response = EditCustomActivePrinciple.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)

    def test_medicine_post_with_patient(self):
        request = self.factory.post('medicine/edit/(?P<pk>[0-9]+)/',
                                    {'name': self.name})
        request.user = self.patient

        with self.assertRaises(PermissionDenied):
            EditCustomActivePrinciple.as_view()(request, pk=1)

    def test_medicine_post_with_health_professional(self):
        request = self.factory.post('medicine/edit/(?P<pk>[0-9]+)/',
                                    {'name': self.name})
        request.user = self.health_professional

        response = EditCustomActivePrinciple.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)
