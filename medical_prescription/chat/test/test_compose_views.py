from django.test import TestCase
from django.test.client import RequestFactory, Client

from chat.views import ComposeView
from user.models import User


class TestComposeView(TestCase):
    """
    Testing methods of Class ComposeView.
    """
    def setUp(self):

        # Creating user in database.
        self.user = User()
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
        self.client = Client()

        self.client.force_login(User.objects.get_or_create(email='test@user.com')[0])
        self.user = User.objects.create_user(email='javed@javed.com', password='my_secret')

    # Testing method 'get' in CreateCustomExamsView.
    def test_get(self):
        request = self.factory.get('/chat/compose/')
        response = self.my_view.get(request)
        request.user = self.user
        self.assertEqual(response.status_code, 200)
"""
    def test_post(self):
        request = self.factory.get('/chat/compose/')
        request.user = self.user

        user_to_email = "test@test.com"
        user_to = User.objects.get(email=user_to_email)
        response = self.client.post('/chat/compose/', {'user_to': user_to, 'text': self.text,
                                                       'subject': self.subject})
        self.assertEqual(response.status_code, 200)
"""
