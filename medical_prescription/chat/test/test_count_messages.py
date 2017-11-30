from django.test import TestCase, RequestFactory
from user.models import User
from chat.models import Response
from chat.views import CountMessagesView


class TestCountMessagesView(TestCase):

    def setUp(self):
        self.user = User()
        self.user.email = "test@test.com"
        self.user.save()

        self.user2 = User()
        self.user2.email = "test2@test.com"
        self.user2.save()

        self.response = Response()
        self.response.user_from = self.user2
        self.response.user_to = self.user
        self.response.save()

        self.factory = RequestFactory()

    def test_get(self, *args, **kwargs):
            request = self.factory.post('/chat/count_messages/ajax', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            request.user = self.user

            response = CountMessagesView.as_view()(request)
            self.assertEquals(response.status_code, 200)
