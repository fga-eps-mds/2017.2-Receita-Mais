from django.db import models
from user.models import HealthProfessional
from medicine.models import ActivePrinciple
#  This class create objects custons active principle


class CustomActivePrinciple(ActivePrinciple):
    created_by = models.ForeignKey(HealthProfessional)
