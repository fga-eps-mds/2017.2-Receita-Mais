from django.test import TestCase
from .models import ActivePrinciple
from .forms import CustomActivePrincipleForm
from .models import CustomActivePrinciple
from user.models import HealthProfessional


class ListActivePrincipleViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/medicine/list/')

    def test_get_active_principle(self):
        self.assertTrue('list_active_principle' in self.resp.context)

    def test_active_principle_str(self):
        principle = ActivePrinciple()
        principle.name = 'Dipirona'
        teste_str = str(principle)
        self.assertEquals(teste_str, 'Dipirona')


class TestCreateCustomActivePrincipleForm(TestCase):
    def setUp(self):
        self.my_view = CustomActivePrincipleForm()
        self.name_valid = "Alguma coisa"
        self.name_exists = "Invalido"

        self.name_max = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                                aaaaaaaaaaaaaaaaaaaaaaaa+1"""

        custom_principle = CustomActivePrinciple()
        custom_principle.name = "Teste"
        user = HealthProfessional()
        user.crm = "54321"
        user.save()
        custom_principle.created_by = user
        custom_principle.save()

    def test_invalid_max_name(self):
        form_data = {'name': self.name_max, }
        form = CustomActivePrincipleForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_valid_max_name(self):
        form_data = {'name': self.name_valid, }
        form = CustomActivePrincipleForm(data=form_data)
        self.assertTrue(form.is_valid())
