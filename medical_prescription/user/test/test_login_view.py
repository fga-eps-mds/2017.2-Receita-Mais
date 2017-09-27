from django.test import TestCase

from user.models import User
from django.test.client import RequestFactory, Client
from user.views import LoginView


class LoginViewTest(TestCase):
    """
    Testing methods of Class LoginView.
    """
    def setUp(self):

        # Creating user in database.
        self.user = User()
        self.user.email = "teste@teste.com"
        self.user.password = "teste404"
        self.user.save()

        self.factory = RequestFactory()
        self.my_view = LoginView()
        self.client = Client()

    # Testind method 'get' in LoginView.
    def test_get(self):
        request = self.factory.get('user/login/')
        response = self.my_view.get(request)

        self.assertEqual(response.status_code, 200)

    # Testing method 'post' in LoginView.
    def test_post(self):
        response = self.client.post('/user/login/', {'email': 'teste@teste.com', 'password': 'teste404'})

        # If the method redirect correctly the status code 200 is returned.
        self.assertEqual(response.status_code, 200)
