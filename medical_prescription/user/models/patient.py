# Django
from django.db import models
from django.core.validators import MaxValueValidator
# Local Django
from .user import User
from .usermanager import UserManager


class Patient(User):
    CPF_document = models.CharField(blank=False, max_length=11, default='')
    CEP = models.PositiveIntegerField(blank=False, default=1, validators=[MaxValueValidator(99999999)])
    UF = models.CharField(blank=False, max_length=2, default='')
    city = models.CharField(blank=False, max_length=50, default='')
    neighborhood = models.CharField(blank=False, max_length=50, default='')
    complement = models.CharField(blank=False, max_length=200, default='')
    objects = UserManager()
