from django.test import TestCase, RequestFactory
from user.models import HealthProfessional
from chat.models import Message
from chat.views import OutboxView


class TestOutbox(TestCase):
    def setUp(self):

        self.professional = HealthProfessional.objects.create(name='Heatlh',
                                                              crm='12345',
                                                              email='healt@heatl.com',
                                                              sex='M',
                                                              is_active=True)

        self.professional2 = HealthProfessional.objects.create(name='UserTest',
                                                               crm='12334',
                                                               email='teste@test.com',
                                                               sex='M',
                                                               is_active=True)
        # Create Message.
        self.message = Message()
        self.message.text = "meu texto"
        self.message.subject = "Assunto"
        self.message.user_from = self.professional
        self.message.user_to = self.professional
        self.message.save()

        self.factory = RequestFactory()
        self.view = OutboxView()

    def test_chat_query_set_true(self):
        request = self.factory.get('chat/outbox')
        request.user = self.professional

        self.view.request = request

        query = self.view.get_queryset()
        self.assertTrue(query.exists())

    def test_chat_query_set_false(self):
        request = self.factory.get('chat/outbox')
        request.user = self.professional2

        self.view.request = request

        query = self.view.get_queryset()
        self.assertFalse(query.exists())
