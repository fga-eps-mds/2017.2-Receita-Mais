from django.db import models

from user.models import Patient
from disease.models import Disease
from exam.models import Exam


class Prescription(models.Model):
    patient = models.ForeignKey(Patient)
    cid = models.ForeignKey(Disease)


class PrescriptionExam(models.Model):
    prescription = models.ForeignKey(Prescription)
    exam = models.ForeignKey(Exam)
