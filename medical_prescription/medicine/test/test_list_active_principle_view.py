# Django
from django.test import TestCase

from medicine.models import ActivePrinciple


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
