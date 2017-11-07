# Django
from django.db import models

# Django Local
from disease.models import Disease


class Prescription(models.Model):
    """
    Prescription model that contains patient and cid to prescription.
    """
    cid = models.ForeignKey(Disease, null=True, blank=True)
