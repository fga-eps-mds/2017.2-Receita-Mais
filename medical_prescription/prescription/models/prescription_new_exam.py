# Django
from django.db import models
from exam.models import NewExam
from prescription.models import Prescription


class PrescriptionNewExam(models.Model):

    prescription = models.ForeignKey(Prescription)
    exam = models.ForeignKey(NewExam)
