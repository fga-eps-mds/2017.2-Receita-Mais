from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from time import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_active, is_superuser, **extra_fields):
        now = timezone.now()

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(
            email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser,
            last_login=now, date_join=now, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password, is_staff, is_active, is_superuser, **extra_fields):
        return self._create_user(self, password, False, False, **extra_fields)

    def create_super_user(self, email, password, is_staff, is_active, is_superuser, **extra_fields):
        return self._create_user(self, password, True, True, **extra_fields)


class User(AbstractBaseUser):
    first_name = models.CharField(blank=False, max_length=50)
    last_name = models.CharField(blank=False, max_length=50)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=11, blank=True)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=10)

    USER_FIELD = 'email'
    REQUIER_FIELDS = ['username', 'first_name', 'last_name', 'date_of_birth', 'sex']

    objects = UserManager()

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name


class HealthProfessional(models.Model):
    user = models.OneToOneField(User)
    crm = models.CharField(max_length=10)
    crm_state = models.CharField(max_length=2)
