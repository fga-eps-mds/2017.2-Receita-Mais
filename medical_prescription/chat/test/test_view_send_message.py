from django.test import TestCase, RequestFactory, Client
from chat.views import SentMessageDetailView
from chat.models import Message, Response
from user.models import HealthProfessional, Patient


class TestSentMessageDetailView(TestCase):

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

        self.view = SentMessageDetailView()
        self.view_class = SentMessageDetailView
        self.factory = RequestFactory()
        self.client = Client()

        self.response = Response()
        self.response.user_from = self.health_professional
        self.response.user_to = self.patient
        self.response.save()

        # Create Message.
        self.message = Message()
        self.message.text = "meu texto"
        self.message.subject = "Assunto"
        self.message.user_from = self.health_professional
        self.message.user_to = self.patient
        self.message.pk = 1
        self.message.messages.add(self.response)
        self.message.save()

    def test_chat_queryset_true(self):
        request = self.view_class.as_view()
        request.user = self.health_professional

        self.view.request = request
        query = self.view.get_queryset()
        self.assertTrue(query.exists())

    def test_chat_get_context_true(self):
        request = self.factory.get('/')
        request.user = self.health_professional
        self.view.request = request
        self.view.object = self.message
        self.assertEqual(type(self.view.get_context_data()), type(dict()))

    def test_chat_get(self):
        request = self.factory.get('/chat/view_sent_message/1')

        request.user = self.health_professional
        self.view.request = request
        self.view.object = self.message

        response = SentMessageDetailView.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_chat_post_true(self):
        request = self.factory.post('/',
                                    {'text': 'isso e um texto',
                                     'user_to': 'test@teste.com',
                                     'user_from': 'teste@teste.com'})
        request.user = self.health_professional
        self.view.request = request
        self.view.object = self.message

        response = self.view_class.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)

    def test_chat_post_false(self):
        request = self.factory.post('/',
                                    {'user_to': 'test@teste.com',
                                     'user_from': 'teste@teste.com'})
        request.user = self.health_professional
        self.view.request = request
        self.view.object = self.message

        response = self.view_class.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)
