from django.test import TestCase

from user.models import User
from django.test.client import RequestFactory, Client
from user.views import ConfirmPasswordView


class TestConfirmPasswordView(TestCase):

    def setUp(self):

        # Creating user in database.
        self.user = User()
        self.user.email = "teste@teste.com"
        self.user.password = "teste"
        self.user.save()

        self.factory = RequestFactory()
        self.my_view = ConfirmPasswordView()
        self.client = Client()

    # Testind method 'get'.
    def test_user_get(self):
        request = self.factory.get('user/reset_confirm/')
        response = self.my_view.get(request)

        self.assertEqual(response.status_code, 200)

    # Testing method 'post'.
    def test_user_post(self):
        response = self.client.post('/user/reset_confirm/', {'password_confirmation': 'teste', 'password': 'teste404'})

        self.assertEqual(response.status_code, 404)

    # Testing method 'post'.
    def test_user_post_(self):
        response = self.client.post('/user/reset_confirm/', {'password_confirmation': 'teste', 'password': 'teste'})

        self.assertEqual(response.status_code, 404)
