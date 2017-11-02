from django.db import models

from exam.models import DefaultExam
from prescription.models import Prescription


class PrescriptionDefaultExam(models.Model):
    prescription = models.ForeignKey(Prescription)
    exam = models.ForeignKey(DefaultExam)
