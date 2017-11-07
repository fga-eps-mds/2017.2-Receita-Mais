# Django
from django.db import models

# Django Local
from disease.models import Disease
from user.models import HealthProfessional


class Prescription(models.Model):
    """
    Prescription base model.
    """
    cid = models.ForeignKey(Disease, null=True, blank=True)
    health_professional = models.ForeignKey(HealthProfessional, related_name='health_professsional',
                                            on_delete=models.CASCADE)
