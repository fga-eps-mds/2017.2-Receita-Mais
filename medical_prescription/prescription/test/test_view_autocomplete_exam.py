# django
from django.test import TestCase
from django.test.client import RequestFactory
from django.http import HttpResponse
from django.test.client import Client

# local djngo.
from prescription.views import AutoCompleteExam
from user.models import HealthProfessional
from exam.models import (Exam,
                         CustomExam)


class TestRequiredAutocompleteExam(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com',
                                                                          password='senha12')
        self.exam = Exam()
        self.exam.description = "Exam Test"
        self.exam.id_tuss = "ID-001"
        self.exam.save()

        self.custom_exam = CustomExam()
        self.custom_exam.name = 'Custom'
        self.custom_exam.health_professional_FK = self.health_professional
        self.custom_exam.description = "Custom"
        self.custom_exam.save()

    def test_prescription_request_autocomplete_exam_fail(self):
        request = self.factory.get('/prescription/ajax/autocomplete_exam/?term=Exa')
        request.user = self.health_professional
        response = AutoCompleteExam.as_view()(request)
        self.assertNotEquals(response, HttpResponse)

    def test_prescription_request_autocomplete_exam_return_no_exam(self):
        request = self.factory.get('/prescription/ajax/autocomplete_exam/?term=out',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.health_professional
        response = AutoCompleteExam.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_prescription_request_autocomplete_exam_return_one_exam(self):
        request = self.factory.get('/prescription/ajax/autocomplete_exam/?term=Exa',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.health_professional
        response = AutoCompleteExam.as_view()(request)
        # response.content
        self.assertEquals(response.status_code, 200)

    def test_prescription_request_autocomplete_exam_return_one_custom_exam(self):
        request = self.factory.get('/prescription/ajax/autocomplete_exam/?term=Cus',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.health_professional
        response = AutoCompleteExam.as_view()(request)
        # response.content
        self.assertEquals(response.status_code, 200)
