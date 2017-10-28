from django.test import TestCase, RequestFactory, Client
from chat.views import SentMessageDetailView
from chat.models import Message
from user.models import HealthProfessional


class TestSentMessageDetailView(TestCase):

    def setUp(self):

        self.user = HealthProfessional.objects.create(name='User Test',
                                                      email='test@teste.com',
                                                      sex='M',
                                                      phone='1111111111',
                                                      is_active=True)
        self.view = SentMessageDetailView()
        self.view_class = SentMessageDetailView
        self.factory = RequestFactory()
        self.client = Client()
        # Create Message.

        self.message = Message()
        self.message.text = "meu texto"
        self.message.subject = "Assunto"
        self.message.user_from = self.user
        self.message.user_to = self.user
        self.message.pk = '1'
        self.message.save()

    def test_queryset_true(self):
        request = self.view_class.as_view()
        request.user = self.user

        self.view.request = request
        query = self.view.get_queryset()
        self.assertTrue(query.exists())

    def test_get_context_true(self):
        request = self.factory.get('/')
        request.user = self.user
        self.view.request = request
        self.view.object = self.message
        self.assertEqual(type(self.view.get_context_data()), type(dict()))

    def test_post_true(self):
        request = self.factory.post('/',
                                    {'text': 'isso e um texto',
                                     'user_to': 'test@teste.com',
                                     'user_from': 'teste@teste.com'})
        request.user = self.user
        self.view.request = request
        self.view.object = self.message

        response = self.view_class.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)

    def test_post_false(self):
        request = self.factory.post('/',
                                    {'user_to': 'test@teste.com',
                                     'user_from': 'teste@teste.com'})
        request.user = self.user
        self.view.request = request
        self.view.object = self.message

        response = self.view_class.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)
