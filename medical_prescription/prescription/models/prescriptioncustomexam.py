# Django
from django.db import models

# Django Local
from exam.models import CustomExam
from prescription.models import Prescription


class PrescriptionCustomExam(models.Model):
    """
    Model to associate prescription to Custom Exam many to many cardinality.
    """
    prescription = models.ForeignKey(Prescription)
    exam = models.ForeignKey(CustomExam)
