from django.test import TestCase, RequestFactory

# Local
from user.models import User
from chat.views import CountMessagesView
from chat.models import Message, Response


class TestCount(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(email='teste@teste.com', password='teste')
        self.factory = RequestFactory()

        self.response = Response()
        self.response.as_read = False
        self.response.user_to = self.user
        self.response.user_from = self.user
        self.response.text = "a"
        self.response.id = 1
        self.response.save()

        # Create Message.
        self.message = Message()
        self.message.id = 1
        self.message.text = "meu texto"
        self.message.subject = "Assunto"
        self.message.user_from = self.user
        self.message.user_to = self.user
        self.message.messages.add(self.response)
        self.message.save()

    def test_get(self):

        request = self.factory.post('/chat/count_message/ajax',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        request.user = self.user
        response = CountMessagesView.as_view()(request)

        self.assertEquals(response.status_code, 200)

    def test_get_invalid(self):
        request = self.factory.post('/chat/count_message/ajax')

        request.user = self.user
        response = CountMessagesView.as_view()(request)

        self.assertNotEquals(response, 200)