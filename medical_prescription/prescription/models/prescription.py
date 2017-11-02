# Django
from django.db import models

# Django Local
from disease.models import Disease
from user import constants


class Prescription(models.Model):
    patient = models.CharField(max_length=constants.NAME_MAX_LENGHT)
    cid = models.ForeignKey(Disease, null=True, blank=True)
