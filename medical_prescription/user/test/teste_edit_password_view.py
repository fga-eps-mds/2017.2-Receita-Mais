# from django.test import TestCase
#
# from django.test.client import RequestFactory, Client
# from user.models import HealthProfessional
# from user.views import UpdateUserPassword
#
#
# class UpdatePasswordViewTest(TestCase):
#     """
#     Testing methods of Class LoginView.
#     """
#     def setUp(self):
#
#         self.user = HealthProfessional()
#         self.user.email = "test@test.com"
#         self.user.password = "test404"
#         self.user.crm = "54321"
#         self.user.save()
#
#         self.factory = RequestFactory()
#         self.my_view = UpdateUserPassword()
#         self.client = Client()
#
#     def test_get_edit_health_professional_password(self):
#         request = self.factory.get('/user/editpasswordhealthprofessional/test@test.com/')
#         response = self.my_view.get(request)
#         self.assertEqual(response.status_code, 200)
#
#     def test_post(self):
#         # request = self.factory.get('/exam/create_custom_exams/')
#         # auth.login(request, self.user)
#         response = self.client.post('/user/editpasswordhealthprofessional/test@test.com/',
#                                     {'old_password':self.user.password , 'password':"12345678" ,
#                                      'password_confirmation':"12345678" })
#         self.assertEqual(response.status_code, 200)
