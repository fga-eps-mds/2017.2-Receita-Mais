from django.test import TestCase, RequestFactory

# Local
from user.models import User
from chat.views import CountMessagesView


class TestCount(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(email='teste@teste.com', password='teste')
        self.factory = RequestFactory()

    def test_get(self):

        request = self.factory.post('/chat/count_message/ajax',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        request.user = self.user
        response = CountMessagesView.as_view()(request)

        self.assertEquals(response.status_code, 200)
