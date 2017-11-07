# Django
from django.db import models

# Django Local
from exam.models import DefaultExam
from prescription.models import Prescription


class PrescriptionDefaultExam(models.Model):
    """
    Model to associate prescription to Default Exam many to many cardinality.
    """
    prescription = models.ForeignKey(Prescription)
    exam = models.ForeignKey(DefaultExam)
