# from django.test import TestCase, Client
#
#
# class TestCompose(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#
#     def test_rendering(self):
#         response = self.client.post('chat/compose/')
#         self.assertTrue(response.status_code, 200)
#
#     def test_compose_view(self):
#         request = self.client.post('chat/ajax/autocomplete_email/', {'felipe'})
#
#         pass
