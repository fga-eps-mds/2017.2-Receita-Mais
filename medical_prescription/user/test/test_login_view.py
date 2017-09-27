from django.test import TestCase
from user.models import User
from django.test.client import RequestFactory, Client
from user.views import LoginView


class LoginViewTest(TestCase):
    def setUp(self):

        # Criando um usuário no banco.
        self.user = User()
        self.user.email = "teste@teste.com"
        self.user.password = "teste404"
        self.user.save()

        self.factory = RequestFactory()
        self.my_view = LoginView()
        self.client = Client()

    # Testando método 'get' de LoginView.
    def test_get(self):
        request = self.factory.get('user/login/')
        response = self.my_view.get(request)

        self.assertEqual(response.status_code, 200)

    # Testando método 'post' de LoginView.
    def test_post(self):
        response = self.client.post('/user/login', {'email': 'teste@teste.com', 'password': 'teste404'})

        # Caso o método redirecione corretamente o código 301 é retornado.
        self.assertEqual(response.status_code, 301)
