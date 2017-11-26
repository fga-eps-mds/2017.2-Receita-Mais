from django.db import models
from user.models import HealthProfessional
#  This class create objects custons active principle


class CustomActivePrinciple(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(HealthProfessional)
