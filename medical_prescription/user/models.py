from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    name = models.CharField(blank=False, max_length=50)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=11, blank=True)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=1)

    is_active = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(User)
    id_document = models.CharField(max_length=32, blank=False)
