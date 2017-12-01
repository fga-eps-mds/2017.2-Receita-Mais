from django.test import TestCase, RequestFactory, Client
from chat.views import UnarchiveMessageHealthProfessionalView
from chat.models import Message
from user.models import HealthProfessional, Patient


class TestUnarchiveMessageHealthProfessionalView(TestCase):

    def setUp(self):

        self.health_professional = HealthProfessional.objects.create(name='User Test',
                                                                     email='test@teste.com',
                                                                     sex='M',
                                                                     phone='1111111111',
                                                                     is_active=True)
        self.patient = Patient.objects.create(name='User Test',
                                              email='testpatient@teste.com',
                                              sex='M',
                                              phone='1111111111',
                                              is_active=True)

        self.view = UnarchiveMessageHealthProfessionalView()
        self.view_class = UnarchiveMessageHealthProfessionalView
        self.factory = RequestFactory()
        self.client = Client()

        # Create Message 1.
        self.message = Message()
        self.message.text = "meu texto"
        self.message.subject = "Assunto"
        self.message.user_from = self.health_professional
        self.message.user_to = self.patient
        self.message.is_active_health_professional = False
        self.message.pk = '1'
        self.message.save()

    def test_post_outbox_true(self):
        request = self.factory.post('/')

        request.user = self.health_professional
        self.view.request = request
        self.view.object = self.message

        message = self.view_class.post(request, pk=1)
        self.assertEqual(message.status_code, 302)
