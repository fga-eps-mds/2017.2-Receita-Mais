# standard library
from datetime import date

# Django
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
# Local Django
from .usermanager import UserManager
from user import constants


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(blank=False, max_length=constants.NAME_MAX_LENGHT, default="")
    date_of_birth = models.DateField(blank=False, default=date.today)
    phone = models.CharField(max_length=constants.PHONE_NUMBER_FIELD_LENGTH_MAX, blank=True)
    email = models.EmailField(unique=True)
    sex = models.CharField(choices=constants.SEX_CHOICE, max_length=10, default=constants.SEX_M)
    image_profile = models.ImageField(upload_to='image_profile/', default=constants.DEFAULT_IMG)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def get_short_name(self):
        return self.name
