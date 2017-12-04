# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied

# Local Django imports
from exam.views import ListExams
from user.models import User, Patient, HealthProfessional


class ListExamsTest(TestCase):
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
        self.user = User.objects.create_user(email='user@user.com', password='senha12')

    def teste_exam_get_exam_without_login(self):
        request = self.factory.get('/exam/list_exams/')
        request.user = AnonymousUser()

        response = ListExams.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def teste_exam_get_exam_with_patient(self):
        request = self.factory.get('/exam/list_exams/')
        request.user = self.patient

        with self.assertRaises(PermissionDenied):
            ListExams.as_view()(request)

    def teste_exam_get_exam_with_user(self):
        request = self.factory.get('/exam/list_exams/')
        request.user = self.user

        with self.assertRaises(PermissionDenied):
            ListExams.as_view()(request)

    def teste_exam_get_exam_with_health_professional(self):
        request = self.factory.get('/exam/list_exams/')
        request.user = self.health_professional

        response = ListExams.as_view()(request)
        self.assertEqual(response.status_code, 200)
