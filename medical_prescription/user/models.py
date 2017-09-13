from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    first_name = models.CharField(blank=False, max_length=50)
    last_name = models.CharField(blank=False, max_length=50)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=11, blank=True)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=10)

    is_active = models.BooleanField(default=False)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name


class HealthProfessional(models.Model):
    user = models.OneToOneField(User)
    crm = models.CharField(max_length=10)
    crm_state = models.CharField(max_length=2)
