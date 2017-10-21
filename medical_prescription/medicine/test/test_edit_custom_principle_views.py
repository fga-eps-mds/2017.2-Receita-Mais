from django.test import TestCase
from django.test.client import RequestFactory, Client

from medicine.views import EditCustomActivePrinciple
from medicine.forms import CustomActivePrincipleForm
from medicine.models import CustomActivePrinciple
from user.models import HealthProfessional


class TestEditCustom(TestCase):
    """
    Testing methods of Class CreateCustomExamsView.
    """

    def setUp(self):
        self.my_view = CustomActivePrincipleForm()
        self.name_valid = "Alguma coisa"
        self.name_exists = "Invalido"

        self.name_max = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                                aaaaaaaaaaaaaaaaaaaaaaaa+1"""

        custom_principle = CustomActivePrinciple()
        custom_principle.name = "Teste"
        custom_principle.pk = "1"
        user = HealthProfessional()
        user.crm = "54321"
        user.save()
        custom_principle.created_by = user
        custom_principle.save()

        self.factory = RequestFactory()
        self.my_view = EditCustomActivePrinciple()
        self.client = Client()

    # Testing method 'post'.
    def test_post(self):
        response = self.client.post('/pt-br/medicine/edit/1/',
                                    {'name': self.name_valid})
        self.assertEqual(response.status_code, 302)

    # Testing method 'post'.
    def test_post_invalid(self):
        response = self.client.post('/medicine/edit/2asdasdasdad/',
                                    {'name': self.name_valid})
        self.assertEqual(response.status_code, 404)
