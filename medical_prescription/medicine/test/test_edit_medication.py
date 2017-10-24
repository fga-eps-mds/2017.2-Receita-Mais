from django.test import TestCase
from medicine.models import Medicine
from medicine.views import UpdateMedicine


class TesteEdit(TestCase):

    def setUp(self):
        self.model = Medicine
        self.view = UpdateMedicine()

    def teste_get_url_sucess(self):
        self.assertEqual(self.view.get_success_url(), '/pt-br/medicine/list_all_medicines/')

    def teste_get_url_false(self):
        self.assertNotEqual(self.view.get_success_url(), 'error')
