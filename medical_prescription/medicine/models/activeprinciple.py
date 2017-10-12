from django.db import models
from user.models import HealthProfessional

#  This class create objects generals active principle


class ActivePrinciple(models.Model):
    name = models.CharField(max_length=100)

#  This class create objects custons active principle


class CustomActivePrinciple(ActivePrinciple):
    created_by = models.ForeignKey('user.HealthProfessional')
