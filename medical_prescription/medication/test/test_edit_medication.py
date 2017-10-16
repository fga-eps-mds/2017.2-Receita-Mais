from django.test import TestCase
from medication.models import Medication
from medication.views import UpdateMedication


class TesteEdit(TestCase):

    def setUp(self):
        self.model = Medication
        self.view = UpdateMedication()

    def teste_get_url_sucess(self):
        self.assertEqual(self.view.get_success_url(), '/medication/list_medication/')

    def teste_get_url_false(self):
        self.assertNotEqual(self.view.get_success_url(), 'error')
