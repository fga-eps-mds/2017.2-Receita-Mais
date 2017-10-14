from django.test import TestCase
from django.test.client import RequestFactory, Client

from exam.views import UpdateCustomExam
from exam.models import CustomExam
from user.models import HealthProfessional


class UpdateCustomExamsViewTest(TestCase):
    """
    Testing methods of Class CreateCustomExamsView.
    """
    def setUp(self):

        # Creating user in database.
        # self.user = HealthProfessional()
        # self.user.email = "test@test.com"
        # self.user.password = "test404"
        # self.user.crm = "54321"
        # self.user.save()

        self.description = "Examina alguma coisa"
        self.name = "Alguma coisa"

        custom_exam = CustomExam()
        custom_exam.name = "Invalido"
        custom_exam.description = "Alguma descricao"
        user = HealthProfessional()
        user.crm = "54321"
        user.save()
        custom_exam.health_professional_FK = user
        custom_exam.pk = 1
        custom_exam.save()

        self.factory = RequestFactory()
        self.my_view = UpdateCustomExam()
        self.client = Client()

    # Testing method 'post' in UpdateCustomExam.
    def test_post(self):
        response = self.client.post('/exam/update_custom_exams/1/',
                                    {'name': self.name, 'description': self.description})
        self.assertEqual(response.status_code, 302)
