from django.test import TestCase, Client, RequestFactory
from user.views import ResetPasswordView
from user.forms import ResetPasswordForm
from user.models import User


class TestResetPassword(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        # Creating user in database.
        self.user = User()
        self.user.email = "teste@teste.com"
        self.user.password = "teste404"
        self.user.is_active = False
        self.user.save()

        self.true_context = {'email': 'teste@teste.com'}
        self.false_context = {'email': 'testeteste.com'}

        self.view = ResetPasswordView()

        self.form = ResetPasswordForm

    def test_user_post_true(self):
        response = self.client.post('/user/reset/')
        self.assertEqual(response.status_code, 200)

    def test_user_get_true(self):
        request = self.factory.get('/user/reset')
        response = self.view.get(request)
        self.assertEqual(response.status_code, 200)

    def test_user_form_true(self):
        request = self.factory.post('user/reset/', self.true_context)
        form = self.form(request.POST)

        self.assertTrue(form.is_valid())
