from django.test import TestCase

from user.models import User


class LoginProfileTest(TestCase):
    """
    Testing user save in database.
    """
    def setUp(self):
        self.user = User()
        self.user.name = "Felipe"
        self.user.date_of_birth = "1995-01-01"
        self.user.phone = "9999-9999"
        self.user.sex = "F"
        self.user.email = "user@user.com"
        self.user.password = "testando"
        self.user.save()

    def test_user_save_name(self):
        self.assertEqual(self.user.name, "Felipe")

    def test_user_save_date_of_birth(self):
        self.assertEqual(self.user.date_of_birth, "1995-01-01")

    def test_user_save_phone(self):
        self.assertEqual(self.user.phone, "9999-9999")

    def test_user_save_sex(self):
        self.assertEqual(self.user.sex, "F")

    def test_user_save_email(self):
        self.assertEqual(self.user.email, "user@user.com")

    def test_user_save_password(self):
        self.assertEqual(self.user.password, "testando")

    def test_user_get_short_name(self):
        user_name = User.objects.get(name="Felipe")
        self.assertEqual(user_name.get_short_name(), "Felipe")
