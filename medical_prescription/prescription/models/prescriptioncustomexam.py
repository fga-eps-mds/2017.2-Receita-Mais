from django.db import models

from exam.models import CustomExam
from prescription.models import Prescription


class PrescriptionCustomExam(models.Model):
    prescription = models.ForeignKey(Prescription)
    exam = models.ForeignKey(CustomExam)
