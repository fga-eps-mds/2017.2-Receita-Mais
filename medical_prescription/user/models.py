from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from . import constants
from datetime import date


class User(AbstractBaseUser):
    USERNAME_FIELD = ['email']
    REQUEIRED_FIELDS = ['name', 'date_of_birth', 'sex', 'email']

    name = models.CharField(blank=False, max_length=50, default="")
    date_of_birth = models.DateField(blank=False, default=date.today)
    phone = models.CharField(max_length=11, blank=False, default='000')
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=1, default='N')

    is_active = models.BooleanField(default=False)


class Patient(models.Model):
    patient = models.OneToOneField(User)
    id_document = models.CharField(blank=False,
                                   max_length=constants.ID_DOCUMENT_MAX_LENGTH)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
