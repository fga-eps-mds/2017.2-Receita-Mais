from django.test import TestCase

from user.models import User, ResetPasswordProfile


class TestPasswordProfile(TestCase):

    def setUp(self):
        # Creating user in database.
        self.user = User()
        self.user.email = "teste@teste.com"
        self.user.password = "teste404"
        self.user.is_active = False
        self.user.name = "usuario"
        self.user.save()

        self.reset_profile = ResetPasswordProfile()
        self.reset_profile.user = self.user
        self.reset_profile.save()

    # Testing user name.
    def test_user_name(self):
        self.assertEqual(self.reset_profile.__str__(), "usuario")
