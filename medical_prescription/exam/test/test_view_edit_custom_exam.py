# Django imports
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied

# Local Django imports
from exam.views import UpdateCustomExam
from exam.models import CustomExam
from user.models import Patient, HealthProfessional


class UpdateCustomExamsViewTest(TestCase):
    """
    Testing methods of Class CreateCustomExamsView.
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

        custom_exam = CustomExam()
        custom_exam.name = "Invalido"
        custom_exam.description = "Alguma descricao"
        custom_exam.health_professional_FK = self.health_professional
        custom_exam.pk = 1
        custom_exam.save()

    # Testing view calls
    def teste_exam_get_without_login(self):
        request = self.factory.get('/exam/update_custom_exams/(?P<pk>[0-9]+)/')
        request.user = AnonymousUser()

        response = UpdateCustomExam.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)

    def teste_exam_get_with_patient(self):
        request = self.factory.get('/exam/update_custom_exams/(?P<pk>[0-9]+)/')
        request.user = self.patient

        with self.assertRaises(PermissionDenied):
            UpdateCustomExam.as_view()(request, pk=1)

    def teste_exam_get_with_health_professional(self):
        request = self.factory.get('/exam/update_custom_exams/(?P<pk>[0-9]+)/')
        request.user = self.health_professional

        response = UpdateCustomExam.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)

    # Testing method 'post' in UpdateCustomExam.
    def teste_exam_post_without_login(self):
        request = self.factory.post('/exam/update_custom_exams/(?P<pk>[0-9]+)/',
                                    {'name': self.name, 'description': self.description})
        request.user = AnonymousUser()

        response = UpdateCustomExam.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)

    def teste_exam_post_with_patient(self):
        request = self.factory.post('/exam/update_custom_exams/(?P<pk>[0-9]+)/',
                                    {'name': self.name, 'description': self.description})
        request.user = self.patient

        with self.assertRaises(PermissionDenied):
            UpdateCustomExam.as_view()(request, pk=1)

    def teste_exam_post_with_health_professional(self):
        request = self.factory.post('/exam/update_custom_exams/(?P<pk>[0-9]+)/',
                                    {'name': self.name, 'description': self.description})
        request.user = self.health_professional

        response = UpdateCustomExam.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)  # Status code isn't '200' because the view is redirected
