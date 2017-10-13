from django.test import TestCase


class ListDiseaseViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/disease/list_disease/')

    def test_get_disease(self):
        self.assertTrue('list_disease' in self.resp.context)
