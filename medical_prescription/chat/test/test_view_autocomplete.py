from django.test import TestCase, Client, RequestFactory
from user.models import HealthProfessional, Patient, AssociatedHealthProfessionalAndPatient
from chat.views import AutoCompleteEmail
from django.http import HttpResponse


class TestAutoComplete(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='test@test.com',
                                                                          password='teste')

        self.patient = Patient.objects.create_user(name="Joao da Silva",
                                                   email='testpatient@test.com',
                                                   password='testepatient')

        self.link = AssociatedHealthProfessionalAndPatient(associated_health_professional=self.health_professional,
                                                           associated_patient=self.patient,
                                                           is_active=True)
        self.link.save()

    def test_chat_request_autocomplete_fail(self):
        request = self.factory.get('/chat/ajax/autocomplete_email/?search=test')
        request.user = self.health_professional
        response = AutoCompleteEmail.as_view()(request)
        self.assertNotEquals(response, HttpResponse)

    def test_chat_request_autocomplete_by_email(self):
        request = self.factory.get('/chat/ajax/autocomplete_email/?search=test',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        request.user = self.health_professional
        response = AutoCompleteEmail.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_chat_request_autocomplete_by_name(self):
        request = self.factory.get('/chat/ajax/autocomplete_email/?search=Joao',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        request.user = self.health_professional
        response = AutoCompleteEmail.as_view()(request)
        self.assertEquals(response.status_code, 200)
