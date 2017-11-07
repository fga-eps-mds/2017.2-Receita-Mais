from django.test import TestCase, RequestFactory, Client
from chat.views import UnarchiveMessageHealthProfessionalView
from chat.models import Message
from user.models import HealthProfessional


class TestUnarchiveMessageHealthProfessionalView(TestCase):

    def setUp(self):

        self.user = HealthProfessional.objects.create(name='User Test',
                                                      email='test@teste.com',
                                                      sex='M',
                                                      phone='1111111111',
                                                      is_active=True)
        self.user2 = HealthProfessional.objects.create(name='UserTest',
                                                               crm='12334',
                                                               email='teste@test.com',
                                                               sex='M',
                                                               is_active=True)
        self.view = UnarchiveMessageHealthProfessionalView()
        self.view_class = UnarchiveMessageHealthProfessionalView
        self.factory = RequestFactory()
        self.client = Client()

        # Create Message 1.
        self.message = Message()
        self.message.text = "meu texto"
        self.message.subject = "Assunto"
        self.message.user_from = self.user
        self.message.user_to = self.user
        self.message.is_active_inbox_health_professional = False
        self.message.is_active_outbox_health_professional = True
        self.message.pk = '1'
        self.message.save()

        # Create Message 2.
        self.message2 = Message()
        self.message2.text = "meu texto"
        self.message2.subject = "Assunto"
        self.message2.user_from = self.user2
        self.message2.user_to = self.user2
        self.message2.is_active_inbox_health_professional = True
        self.message2.is_active_outbox_health_professional = False
        self.message2.pk = '2'
        self.message2.save()

    def test_post_inbox_true(self):
        request = self.factory.post('/')

        request.user = self.user
        self.view.request = request
        self.view.object = self.message

        message = self.view_class.post(request, pk=1)
        self.assertEqual(message.status_code, 302)

    def test_post_outbox_true(self):
        request = self.factory.post('/')

        request.user = self.user2
        self.view.request = request
        self.view.object = self.message

        message = self.view_class.post(request, pk=2)
        self.assertEqual(message.status_code, 302)
