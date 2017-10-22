# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser

# Local Django imports
from medicine.forms import CustomActivePrincipleForm
from medicine.views import CreateCustomActivePrinciple
from user.views import LoginView
from user.models import User, Patient, HealthProfessional


class TestCreateCustom(TestCase):
    """
    Testing methods of Class CreateCustomExamsView.
    """

    def setUp(self):
        self.my_view = CustomActivePrincipleForm()
        self.name_valid = "Alguma coisa"

        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com', password='senha12')
        self.patient = Patient.objects.create_user(email='patient@patient.com', password='senha12')
        self.user = User.objects.create_user(email='user@user.com', password='senha12')
        """
    # Testing method 'get'.
    def test_get(self):
        request = self.factory.get('/medicine/create/')
        response = self.my_view.get(request)

        self.assertEqual(response.status_code, 200)

    # Testing method 'post'.
    def test_post(self):
        self.client.login(email='test@test.com', password='test404')
        response = self.client.post('/medicine/create/',
                                    {'name': self.name_valid, 'created_by': 'test@test.com'})
        self.assertEqual(response.status_code, 302)
        """

    def test_post_without_login(self):
        request = self.factory.post('/medicine/create/', {'name': self.name_valid, 'created_by': 'test@test.com'})
        request.user = AnonymousUser()
        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_post_with_patient(self):
        request = self.factory.post('/medicine/create/', {'name': self.name_valid, 'created_by': 'test@test.com'})
        request.user = self.patient
        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_post_with_user(self):
        request = self.factory.post('/medicine/create/', {'name': self.name_valid, 'created_by': 'test@test.com'})
        request.user = self.user
        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_post_with_health_professional(self):
        request = self.factory.post('/medicine/create/', {'name': self.name_valid, 'created_by': 'doctor@doctor.com'})
        request.user = self.health_professional
        response = CreateCustomActivePrinciple.as_view()(request)
        self.assertEqual(response.status_code, 302)
