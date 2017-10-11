from django.db import models
from user.models import HealthProfessional


class ActivePrinciple(models.Model):
    name = models.CharField(max_length=100)


class CustomActivePrinciple(ActivePrinciple):
    created_by = models.ForeignKey('user.HealthProfessional')
