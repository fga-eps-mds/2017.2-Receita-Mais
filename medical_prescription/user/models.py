# standard library
from datetime import date

# Django
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=self.normalize_email(email),
                          password=password,
                          is_active=True,
                          **kwargs)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=self.normalize_email(email),
                          password=password,
                          is_active=True,
                          is_staff=True,
                          is_superuser=True,
                          **kwargs)

        user.set_password(password)
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(blank=False, max_length=50, default="")
    date_of_birth = models.DateField(blank=False, default=date.today)
    phone = models.CharField(max_length=11, blank=True, default='00000000000')
    email = models.EmailField(unique=True)

    SEX_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )

    sex = models.CharField(blank=False, max_length=1, choices=SEX_CHOICES)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def get_short_name(self):
        return self.name


class Patient(User):
    id_document = models.CharField(blank=False, max_length=32, default='')

    objects = UserManager()
