# standard library
import datetime

# Django
from django.db import models

# Local Django
from .user import User


class ResetPasswordProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.user.name
