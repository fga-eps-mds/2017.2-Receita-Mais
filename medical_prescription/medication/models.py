from django.db import models

from user.models import HealthProfessional


class Medication(models.Model):

    name = models.CharField(max_length=100, blank=False, default="")
    active_ingredient = models.CharField(max_length=100, blank=False, default="")
    laboratory = models.CharField(max_length=100, blank=False, default="")
    description = models.TextField()
    is_restricted = models.BooleanField(default=False)

    health_professional = models.ForeignKey(HealthProfessional)
