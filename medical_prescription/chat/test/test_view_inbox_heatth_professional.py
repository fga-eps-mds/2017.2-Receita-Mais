from django.test import TestCase, RequestFactory
from chat.models import Message
from user.models import Patient, HealthProfessional
from chat.views import InboxHealthProfessionalView


class TesteInboxHealthProfessional(TestCase):

    def setUp(self):

        # Create Patient.
        self.patient = Patient.objects.create(name='Paciente',
                                              phone='1111111111',
                                              email='patient@patient.com',
                                              CEP='72850735',
                                              UF='DF',
                                              city='Brasília',
                                              neighborhood='Asa sul',
                                              complement='Bloco 2 QD 701')
        self.patient.save()

        self.professional = HealthProfessional.objects.create(name='Heatlh',
                                                              crm='12345',
                                                              email='healt@heatl.com',
                                                              sex='M',
                                                              is_active=True)
        self.professional.save()

        self.view = InboxHealthProfessionalView()
        self.factory = RequestFactory()

        # Create Message.
        self.message = Message()
        self.message.text = "meu texto"
        self.message.subject = "Assunto"
        self.message.user_from = self.professional
        self.message.user_to = self.patient
        self.message.save()

    def test_query_true(self):
        request = self.factory.get('/chat/compose/')
        request.user = self.patient

        self.view.request = request

        query = self.view.get_queryset()

        self.assertTrue(query.exists())

    def test_query_false(self):
        request = self.factory.get('/chat/compose/')
        request.user = self.professional

        self.view.request = request

        query = self.view.get_queryset()
        print(query)

        self.assertFalse(query.exists())
