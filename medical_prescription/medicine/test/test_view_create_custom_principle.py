# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from unittest.mock import patch, MagicMock
from django.core.exceptions import PermissionDenied

# Local Django imports
from medicine.forms import CustomActivePrincipleForm
from medicine.views import CreateCustomActivePrinciple
from user.models import Patient, HealthProfessional
from medicine.models import CustomActivePrinciple


class TestCreateCustom(TestCase):
    """
    Testing methods of Class CreateCustomExamsView.
    """

    def setUp(self):
        self.my_view = CustomActivePrincipleForm()
        self.name_valid = "Alguma coisa"

        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com', password='senha12')
        self.patient = Patient.objects.create_user(email='patient@patient.com',
                                                   password='senha12',
                                                   CEP='72850735',
                                                   UF='DF',
                                                   city='Brasília',
                                                   neighborhood='Asa sul',
                                                   complement='Bloco 2 QD 701')

    def test_medicine_get_without_login(self):
        request = self.factory.get('/medicine/create/')
        request.user = AnonymousUser()

        response = CreateCustomActivePrinciple.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_medicine_get_with_patient(self):
        request = self.factory.get('/medicine/create/')
        request.user = self.patient

        with self.assertRaises(PermissionDenied):
            CreateCustomActivePrinciple.as_view()(request)

    def test_medicine_get_with_health_professional(self):
        request = self.factory.get('/medicine/create/')
        request.user = self.health_professional

        response = CreateCustomActivePrinciple.as_view()(request)
        self.assertEqual(response.status_code, 200)

    @patch('medicine.models.CustomActivePrinciple.save', MagicMock(name="save"))
    def test_medicine_post_with_health_professional(self):
        """
        Test post requests
        """
        # Create the request
        data = {
            'name': self.name_valid,
            'created_by': 'doctor@doctor.com'
        }

        request = self.factory.post('/medicine/create/', data)
        request.user = self.health_professional

        # Get the response
        response = CreateCustomActivePrinciple.as_view()(request)
        self.assertEqual(response.status_code, 302)

        # Check save was called
        self.assertTrue(CustomActivePrinciple.save.called)
        self.assertEqual(CustomActivePrinciple.save.call_count, 1)

    @patch('medicine.models.CustomActivePrinciple.save', MagicMock(name="save"))
    def test_medicine_post_without_login(self):
        """
        Test post requests
        """
        # Create the request
        data = {
            'name': self.name_valid,
            'created_by': 'doctor@doctor.com'
        }

        request = self.factory.post('/medicine/create/', data)
        request.user = AnonymousUser()

        # Get the response
        response = CreateCustomActivePrinciple.as_view()(request)
        self.assertEqual(response.status_code, 302)

        # Check save was called
        self.assertFalse(CustomActivePrinciple.save.called)
        self.assertEqual(CustomActivePrinciple.save.call_count, 0)

    @patch('medicine.models.CustomActivePrinciple.save', MagicMock(name="save"))
    def test_medicine_post_with_patient(self):
        """
        Test post requests
        """
        # Create the request
        data = {
            'name': self.name_valid,
            'created_by': 'doctor@doctor.com'
        }

        request = self.factory.post('/medicine/create/', data)
        request.user = self.patient

        # Get the response
        with self.assertRaises(PermissionDenied):
            CreateCustomActivePrinciple.as_view()(request)

        # Check save was called
        self.assertFalse(CustomActivePrinciple.save.called)
        self.assertEqual(CustomActivePrinciple.save.call_count, 0)
