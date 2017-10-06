from django.test import TestCase

from user.models import User
from user.forms import UpdateUserForm


class TestUpdateUserForm(TestCase):

    def setUp(self):
        self.name_valid = 'Teste Nome'
        self.name_invalid = 'a@'
        self.name_invalid_TYPE = 'a@hjasgdjasdal'
        self.name_invalid_MAX = 'aasdkgasdlkasdjkljkjdklasjjasvdashdjavcdbnmhasdvbdmmasbdnmhamsjdhgegdhjgsavdhabvdbnasd'
        self.name_invalid_MIN = 'a'

        self.phone_valid = '1234567890'
        self.phone_invalid = '456'
        self.phone_invalid_MIN = '456'
        self.phone_invalid_TYPE = 'asdaaaaaads'
        self.phone_invalid_MAX = '456134564898761'

        self.password_valid = '1234567'
        self.password_invalid = '123456789'
        self.password_invalid_MAX = '1234567891011'
        self.password_invalid_MIN = '123'
        self.password_invalid_TYPE = 'a@d123a'

        self.date_of_birth_valid = '10/12/1990'
        self.date_of_birth_invalid = '18'
        self.date_of_birth_invalid_FORMAT = '18'
        self.date_of_birth_invalid_MIN = '10/12/2020'

        self.sex_valid = 'M'
        self.sex_invalid = 'A'

        user = User()
        user.email = "admin@hotmail.com"
        user.save()

    def test_update_user_form_valid(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_update_user_form_name_is_not_valid_TYPE(self):
        form_data = {'name': self.name_invalid_TYPE,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid}
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_name_is_not_valid_MAX(self):
        form_data = {'name': self.name_invalid_MAX,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_name_is_not_valid_MIN(self):
        form_data = {'name': self.name_invalid_MIN,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_date_of_birth_is_not_valid_FORMAT(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_invalid_FORMAT,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_date_of_birth_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_invalid_MIN,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_phone_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid_TYPE,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_phone_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid_MIN,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_phone_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid_MAX,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_sex_is_not_valid(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_invalid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_password_is_not_valid_MAX(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_invalid_MAX,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_password_is_not_valid_MIN(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_invalid_MIN}
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_password_is_not_valid_TYPE(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_invalid_TYPE,
                     'confirm_password': self.password_valid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_0(self):
        form_data = {'name': self.name_invalid,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_invalid,
                     'sex': self.sex_invalid,
                     'password': self.password_invalid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_1(self):
        form_data = {'name': self.name_invalid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid,
                     'sex': self.sex_valid,
                     'password': self.password_valid}
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_2(self):
        form_data = {'name': self.name_invalid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_invalid,
                     'password': self.password_valid}
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_3(self):
        form_data = {'name': self.name_invalid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_invalid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_4(self):
        form_data = {'name': self.name_invalid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_5(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_invalid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_6(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_valid,
                     'sex': self.sex_invalid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_7(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_invalid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_8(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_invalid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_9(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid,
                     'sex': self.sex_invalid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_10(self):
        form_data = {'name': self.name_invalid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid,
                     'sex': self.sex_valid,
                     'password': self.password_invalid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_11(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_invalid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_12(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_invalid,
                     'password': self.password_invalid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_13(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_invalid,
                     'password': self.password_valid,
                     }
        form = UpdateUserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_update_user_form_invalid_14(self):
        form_data = {'name': self.name_valid,
                     'date_of_birth': self.date_of_birth_valid,
                     'phone': self.phone_valid,
                     'sex': self.sex_valid,
                     'password': self.password_valid,
                     'confirm_password': self.password_invalid}
        form = UpdateUserForm(data=form_data)
        self.assertFalse(form.is_valid())
