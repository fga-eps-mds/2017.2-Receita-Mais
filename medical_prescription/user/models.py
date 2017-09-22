from datetime import date

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from . import constants


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email),
                          password=password,
                          is_active=True,
                          **extra_fields)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.model(email=self.normalize_email(email),
                          password=password,
                          is_active=True,
                          is_staff=True,
                          is_superuser=True,
                          **extra_fields)

        user.set_password(password)
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(blank=False, max_length=constants.NAME_MAX_LENGHT, default="")
    date_of_birth = models.DateField(blank=False, default=date.today)
    phone = models.CharField(max_length=constants.PHONE_NUMBER_FIELD_LENGTH, blank=True, default='00000000000')
    email = models.EmailField(unique=True)
    sex = models.CharField(choices=constants.SEX_CHOICE, max_length=10, default=constants.SEX_M)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def get_short_name(self):
        return self.name


class HealthProfessional(models.Model):
    user = models.OneToOneField(User)
    crm = models.CharField(max_length=constants.CRM_LENGTH, unique=True)
    crm_state = models.CharField(choices=constants.UF_CHOICE, max_length=constants.CRM_STATE_LENGTH, default='DF')
