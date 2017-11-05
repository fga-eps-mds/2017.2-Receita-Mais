from django.test import TestCase
from medicine.forms import CustomActivePrincipleForm
from medicine.models import CustomActivePrinciple
from user.models import HealthProfessional


class TestCreateCustomActivePrincipleForm(TestCase):
    def setUp(self):
        self.my_view = CustomActivePrincipleForm()
        self.name_valid = "Alguma coisa"
        self.name_exists = "Invalido"

        self.name_max = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                                aaaaaaaaaaaaaaaaaaaaaaaa+1"""

        custom_principle = CustomActivePrinciple()
        custom_principle.name = "test"
        user = HealthProfessional()
        user.crm = "54321"
        user.save()
        custom_principle.created_by = user
        custom_principle.save()

    def test_medicine_invalid_max_name(self):
        form_data = {'name': self.name_max, }
        form = CustomActivePrincipleForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_medicine_valid_max_name(self):
        form_data = {'name': self.name_valid, }
        form = CustomActivePrincipleForm(data=form_data)
        self.assertTrue(form.is_valid())
