from django.test import TestCase, RequestFactory
from chat.models import Response
from user.models import Patient, HealthProfessional
from chat.views import ListPatientFiles


class TestPatient(TestCase):

    def setUp(self):

        # Create Patient.
        self.patient = Patient.objects.create(name='Paciente',
                                              phone='1111111111',
                                              email='patient@patient.com')
        self.patient.save()

        self.professional = HealthProfessional.objects.create(name='Heatlh',
                                                              crm='12345',
                                                              email='healt@heatl.com',
                                                              sex='M',
                                                              is_active=True)
        self.professional.save()

        self.view = ListPatientFiles()
        self.factory = RequestFactory()

        # Create Message.
        self.response = Response()
        self.response.text = "meu texto"
        self.response.subject = "Assunto"
        self.response.user_from = self.patient
        self.response.user_to = self.professional
        self.response.files = "files"
        self.response.save()

    def test_chat_query_true(self):
        request = self.factory.get('/')
        request.user = self.patient

        self.view.request = request

        query = self.view.get_queryset()

        self.assertTrue(query)

    def test_chat_query_false(self):
        request = self.factory.get('/')
        request.user = self.professional

        self.view.request = request

        query = self.view.get_queryset()
        print(query)

        self.assertFalse(query)

    def test_list_prescription(self):
        request = self.factory.get('/')
        request.user = self.patient

        response = ListPatientFiles.as_view()(request)
        self.assertEqual(response.status_code, 200)
