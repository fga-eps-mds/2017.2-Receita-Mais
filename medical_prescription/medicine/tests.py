from django.test import TestCase


class ListActivePrincipleViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/medicine/list/')

    def test_get_active_principle(self):
        self.assertTrue('list_active_principle' in self.resp.context)
