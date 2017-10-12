# standard library
import datetime

# Django
from django.db import models

# Local Django
from .models import User


class UserActivateProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_lenght=50, blank=False)
    key_expire = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = u'Activate Account Profile'
