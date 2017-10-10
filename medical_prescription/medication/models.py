from django.db import models

from user.models import HealthProfessional


class Medication(models.Model):
    description = models.TextField() 
    indication = models.TextField() 
    dosage = models.TextField() 

    health_professional = models.ForeignKey(HealthProfessional)