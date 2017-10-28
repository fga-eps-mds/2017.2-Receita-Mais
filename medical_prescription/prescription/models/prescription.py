from django.db import models

from user.models import Patient
from disease.models import Disease


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, blank=True, null=True)
    cid = models.ForeignKey(Disease, blank=True, null=True)
