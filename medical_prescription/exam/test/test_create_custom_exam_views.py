from django.test import TestCase
from django.test.client import RequestFactory, Client

from exam.views import CreateCustomExamsView
from user.models import HealthProfessional


class CreateCustomExamsViewTest(TestCase):
    """
    Testing methods of Class CreateCustomExamsView.
    """
    def setUp(self):

        # Creating user in database.
        self.user = HealthProfessional()
        self.user.email = "test@test.com"
        self.user.password = "test404"
        self.user.crm = "54321"
        self.user.save()

        self.description = "Examina alguma coisa"
        self.name = "Alguma coisa"

        self.factory = RequestFactory()
        self.my_view = CreateCustomExamsView()
        self.client = Client()

    # Testing method 'get' in CreateCustomExamsView.
    def test_get(self):
        request = self.factory.get('/exam/create_custom_exams/')
        response = self.my_view.get(request)

        self.assertEqual(response.status_code, 200)

    def test_post(self):
        # request = self.factory.get('/exam/create_custom_exams/')
        # auth.login(request, self.user)
        response = self.client.post('/exam/create_custom_exams/', {'name': '', 'description': self.description})
        self.assertEqual(response.status_code, 200)
