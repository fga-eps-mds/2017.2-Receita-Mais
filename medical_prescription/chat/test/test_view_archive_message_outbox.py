from django.test import TestCase, RequestFactory, Client
from chat.views import ArchiveMessageOutboxView
from chat.models import Message
from user.models import HealthProfessional


class TestArchiveMessageOutboxView(TestCase):

    def setUp(self):

        self.user = HealthProfessional.objects.create(name='User Test',
                                                      email='test@teste.com',
                                                      sex='M',
                                                      phone='1111111111',
                                                      is_active=True)
        self.view = ArchiveMessageOutboxView()
        self.view_class = ArchiveMessageOutboxView
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

    def test_post_true(self):
        request = self.factory.post('/')

        request.user = self.user
        self.view.request = request
        self.view.object = self.message

        message = self.view_class.post(request, pk=1)
        self.assertEqual(message.status_code, 302)
