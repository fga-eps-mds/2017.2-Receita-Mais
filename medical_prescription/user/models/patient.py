# Django
from django.db import models

# Local Django
from .user import User
from .usermanager import UserManager


class Patient(User):
    id_document = models.CharField(blank=False, max_length=32, default='')

    objects = UserManager()
