from django.test import TestCase, Client, RequestFactory
from user.models import User
from chat.views import AutoCompleteEmail
from django.http import HttpResponse


class TestAutoComplete(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.health_professional = User.objects.create_user(email='test@test.com',
                                                            password='teste')

    def test_request_autocomplete_cid_fail(self):
        request = self.factory.get('/chat/ajax/autocomplete_email/?search=test')
        request.user = self.health_professional
        response = AutoCompleteEmail.as_view()(request)
        self.assertNotEquals(response, HttpResponse)

    def test_request_autocomplete_cid_return_one_disease(self):
        request = self.factory.get('/chat/ajax/autocomplete_email/?search=test',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        request.user = self.health_professional
        response = AutoCompleteEmail.as_view()(request)
        self.assertEquals(response.status_code, 200)
