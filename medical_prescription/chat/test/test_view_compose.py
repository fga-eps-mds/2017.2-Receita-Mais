from django.test import TestCase
from django.test.client import RequestFactory, Client

from chat.views import ComposeView
from user.models import HealthProfessional


class TestComposeView(TestCase):
    """
    Testing methods of Class ComposeView.
    """
    def setUp(self):

        # Creating user in database.
        self.user = HealthProfessional()
        self.user.email = "test@test.com"
        self.user.password = "test404"
        self.user.save()

        self.user_to_invalid = "test@test"
        self.user_to = "test@test.com"
        self.user_from = "test@test.com"
        self.text = "a"
        self.subject = "a"

        self.factory = RequestFactory()
        self.my_view = ComposeView()
        self.my_view_class = ComposeView
        self.client = Client()

    def test_get(self):
        request = self.factory.get('/chat/compose/')
        request.user = self.user
        response = self.my_view.get(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = self.factory.post('chat/compose',
                                    {'text': 'isso e um texto',
                                     'subject': 'test suject',
                                     'user_to': 'test@test.com',
                                     'user_to': 'test@test.com'})
        request.user = self.user

        response = self.my_view_class.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_post_invalid(self):
        request = self.factory.post('chat/compose',
                                    {'text': 'a'*10000,
                                     'subject': 'test suject',
                                     'user_to': 'test@test.com',
                                     'user_to': 'test@test.com'})
        request.user = self.user

        response = self.my_view_class.as_view()(request)
        self.assertEqual(response.status_code, 200)
