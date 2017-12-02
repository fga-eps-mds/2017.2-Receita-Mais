# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied

# Local Django imports
from user.views import UpdateUserPassword
from user.models import User, Patient, HealthProfessional


class TestUpdateHealthProfessionalPassword(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com',
                                                                          password='senha12')

        self.patient = Patient.objects.create_user(email='patient@patient.com',
                                                   password='senha12',
                                                   CEP='72850735',
                                                   UF='DF',
                                                   city='Brasília',
                                                   neighborhood='Asa sul',
                                                   complement='Bloco 2 QD 701')

        self.user = User.objects.create_user(email='user@user.com',
                                             password='senha12')

    def test_user_get_health_professional_with_patient(self):
        request = self.factory.get('user/editpasswordhealthprofessional/(?P<email>[\w|\W]+)')
        request.user = self.patient

        with self.assertRaises(PermissionDenied):
            UpdateUserPassword.edit_health_professional_password_view(request,
                                                                      email=self.health_professional.email)

    def test_user_get_health_professional_with_user(self):
        request = self.factory.get('user/editpasswordhealthprofessional/(?P<email>[\w|\W]+)')
        request.user = self.user

        with self.assertRaises(PermissionDenied):
            UpdateUserPassword.edit_health_professional_password_view(request,
                                                                      email=self.health_professional.email)

    def test_user_get_health_professional_with_own_health_professional(self):
        request = self.factory.get('user/editpasswordhealthprofessional/(?P<email>[\w|\W]+)')
        request.user = self.health_professional

        response = UpdateUserPassword.edit_health_professional_password_view(request,
                                                                             email=self.health_professional.email)
        self.assertEqual(response.status_code, 200)

    def test_user_get_health_professional_with_health_professional(self):
        request = self.factory.get('user/editpasswordhealthprofessional/(?P<email>[\w|\W]+)')
        request.user = self.health_professional

        with self.assertRaises(PermissionDenied):
            UpdateUserPassword.edit_health_professional_password_view(request,
                                                                      email='teste@teste.com')

    def post_without_login(self):
        request = self.factory.post('user/editpasswordhealthprofessional/(?P<email>[\w|\W]+)')
        request.user = AnonymousUser()

        response = UpdateUserPassword.edit_health_professional_password_view(request,
                                                                             email=self.health_professional.email)
        self.assertEqual(response.status_code, 302)

    def test_user_post_health_professional_with_patient(self):
        request = self.factory.post('user/editpasswordhealthprofessional/(?P<email>[\w|\W]+)')
        request.user = self.patient

        with self.assertRaises(PermissionDenied):
            UpdateUserPassword.edit_health_professional_password_view(request,
                                                                      email=self.health_professional.email)

    def test_user_post_health_professional_with_user(self):
        request = self.factory.post('user/editpasswordhealthprofessional/(?P<email>[\w|\W]+)')
        request.user = self.user

        with self.assertRaises(PermissionDenied):
            UpdateUserPassword.edit_health_professional_password_view(request,
                                                                      email=self.health_professional.email)

    def test_user_post_health_professional_with_own_health_professional(self):
        request = self.factory.post('user/editpasswordhealthprofessional/(?P<email>[\w|\W]+)')
        request.user = self.health_professional

        response = UpdateUserPassword.edit_health_professional_password_view(request,
                                                                             email=self.health_professional.email)
        self.assertEqual(response.status_code, 200)

    def test_user_post_health_professional_with_health_professional(self):
        request = self.factory.post('user/editpasswordhealthprofessional/(?P<email>[\w|\W]+)')
        request.user = self.health_professional

        with self.assertRaises(PermissionDenied):
            UpdateUserPassword.edit_health_professional_password_view(request,
                                                                      email='teste@teste.com')


class UpdatePatientPassword(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com',
                                                                          password='senha12')

        self.patient = Patient.objects.create_user(email='patient@patient.com',
                                                   password='senha12',
                                                   CEP='72850735',
                                                   UF='DF',
                                                   city='Brasília',
                                                   neighborhood='Asa sul',
                                                   complement='Bloco 2 QD 701')

        self.user = User.objects.create_user(email='user@user.com',
                                             password='senha12')

    def _without_login(self):
        request = self.factory.get('user/editpasswordpatient/(?P<email>[\w|\W]+)')
        request.user = AnonymousUser()

        response = UpdateUserPassword.edit_patient_password_view(request,
                                                                 email=self.patient.email)
        self.assertEqual(response.status_code, 302)

    def test_user_edit_patient_with_user(self):
        request = self.factory.get('user/editpasswordpatient/(?P<email>[\w|\W]+)')
        request.user = self.user

        with self.assertRaises(PermissionDenied):
            UpdateUserPassword.edit_patient_password_view(request,
                                                          email=self.patient.email)

    def test_user_edit_patient_with_health_professional(self):
        request = self.factory.get('user/editpasswordpatient/(?P<email>[\w|\W]+)')
        request.user = self.health_professional

        with self.assertRaises(PermissionDenied):
            UpdateUserPassword.edit_patient_password_view(request,
                                                          email=self.patient.email)

    def test_user_edit_patient_with_own_patient(self):
        request = self.factory.get('user/editpasswordpatient/(?P<email>[\w|\W]+)')
        request.user = self.patient

        response = UpdateUserPassword.edit_patient_password_view(request,
                                                                 email=self.patient.email)
        self.assertEqual(response.status_code, 200)

    def test_user_edit_patient_with_patient(self):
        request = self.factory.get('user/editpasswordpatient/(?P<email>[\w|\W]+)')
        request.user = self.patient

        with self.assertRaises(PermissionDenied):
            UpdateUserPassword.edit_patient_password_view(request,
                                                          email='teste@teste.com')

    def post_without_login(self):
        request = self.factory.post('user/editpasswordpatient/(?P<email>[\w|\W]+)')
        request.user = AnonymousUser()

        response = UpdateUserPassword.edit_patient_password_view(request,
                                                                 email=self.health_professional.email)
        self.assertEqual(response.status_code, 302)

    def test_user_post_patient_with_patient(self):
        request = self.factory.post('user/editpasswordpatient/(?P<email>[\w|\W]+)')
        request.user = self.patient

        with self.assertRaises(PermissionDenied):
            UpdateUserPassword.edit_patient_password_view(request,
                                                          email="teste@teste.com")

    def test_user_post_patient_with_user(self):
        request = self.factory.post('user/editpasswordpatient/(?P<email>[\w|\W]+)')
        request.user = self.user

        with self.assertRaises(PermissionDenied):
            UpdateUserPassword.edit_patient_password_view(request,
                                                          email=self.patient.email)

    def test_user_post_patient_with_own_patient(self):
        request = self.factory.post('user/editpasswordpatient/(?P<email>[\w|\W]+)')
        request.user = self.patient

        response = UpdateUserPassword.edit_patient_password_view(request,
                                                                 email=self.patient.email)
        self.assertEqual(response.status_code, 200)

    def test_user_post_patient_with_health_professional(self):
        request = self.factory.post('user/editpasswordpatient/(?P<email>[\w|\W]+)')
        request.user = self.health_professional

        with self.assertRaises(PermissionDenied):
            UpdateUserPassword.edit_patient_password_view(request,
                                                          email=self.health_professional.email)
