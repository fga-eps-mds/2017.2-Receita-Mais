# Django
from django.db import models

# Local Django
from user.models import HealthProfessional, Patient


class AssociatedHealthProfessionalAndPatient(models.Model):
    associated_patient = models.ForeignKey(Patient)
    associated_health_professional = models.ForeignKey(HealthProfessional)
    is_active = models.BooleanField(default=False)
