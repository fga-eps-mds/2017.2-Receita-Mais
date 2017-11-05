from django.test import TestCase
from user.views import ResetPasswordView
from user.models import ResetPasswordProfile, User


class TestViewRecoverProfile(TestCase):

    def setUp(self):
        self.view = ResetPasswordView
        self.model = ResetPasswordProfile

        # Creating user in database.
        self.user = User()
        self.user.email = "teste@teste.com"
        self.user.password = "teste404"
        self.user.is_active = False
        self.user.name = "usuario"
        self.user.save()

    # Test if ResetPasswordProfile are save databe.
    def test_user_create_recover_profile(self):

        recover = self.view._create_recover_profile(self.view, self.user)
        recover.save()
        query = ResetPasswordProfile.objects.filter(pk=recover.pk)

        self.assertTrue(query.exists())
