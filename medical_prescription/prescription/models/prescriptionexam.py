from django.db import models

from exam.models import Exam
from prescription.models import Prescription


class PrescriptionExam(models.Model):
    prescription = models.ForeignKey(Prescription)
    exam = models.ForeignKey(Exam)
