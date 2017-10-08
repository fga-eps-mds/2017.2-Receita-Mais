from django.test import TestCase

from user.models import User


class TestUserManager(TestCase):

    def setUp(self):
        self.user = User()
        self.email = 'admin@admin.com'
        self.password = '123456a'

    def test_user_manager(self):
        User.objects.create_superuser(email=self.email, password=self.password)
        user = User.objects.filter(email=self.email)
        self.assertTrue(user.exists())
