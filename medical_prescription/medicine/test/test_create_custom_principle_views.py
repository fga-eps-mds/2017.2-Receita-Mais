from django.test import TestCase
from django.test.client import RequestFactory, Client

from medicine.forms import CustomActivePrincipleForm
from medicine.models import CustomActivePrinciple
from user.models import HealthProfessional


class TestCreateCustom(TestCase):
    """
    Testing methods of Class CreateCustomExamsView.
    """

    def setUp(self):
        self.my_view = CustomActivePrincipleForm()
        self.name_valid = "Alguma coisa"
        self.name_exists = "Invalido"

        self.name_max = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                                aaaaaaaaaaaaaaaaaaaaaaaa+1"""

        user = HealthProfessional()
        user.crm = "54321"
        user.email = "test@test.com"
        user.password = "test404"
        user.pk = '1'
        user.save()

        custom_principle = CustomActivePrinciple()
        custom_principle.name = "Teste"
        custom_principle.pk = "1"
        custom_principle.created_by = user
        custom_principle.save()

        self.factory = RequestFactory()
        self.my_view = CustomActivePrincipleForm()
        self.client = Client()
        self.client.login(email='test@test.com', password='test404')
        """
    # Testing method 'get'.
    def test_get(self):
        request = self.factory.get('/medicine/create/')
        response = self.my_view.get(request)

        self.assertEqual(response.status_code, 200)

    # Testing method 'post'.
    def test_post(self):
        self.client.login(email='test@test.com', password='test404')
        response = self.client.post('/medicine/create/',
                                    {'name': self.name_valid, 'created_by': 'test@test.com'})
        self.assertEqual(response.status_code, 302)
        """
    # Testing method 'post'.
    def test_post_invalid(self):
        response = self.client.post('/medicine/create/asdasd',
                                    {'name': self.name_valid, 'created_by': 'test@test.com'})
        self.assertEqual(response.status_code, 404)
