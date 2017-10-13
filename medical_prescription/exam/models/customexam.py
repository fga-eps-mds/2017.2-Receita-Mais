# Django
from django.db import models

# Local Django
from .exam import Exam
from exam import constants
from user.models import HealthProfessional


class CustomExam(Exam):
    class Meta:
        unique_together = (('name', 'health_professional_FK'),)

    name = models.CharField(max_length=constants.NAME_MAX_LENGTH, unique=True, default="")
    health_professional_FK = models.ForeignKey(HealthProfessional, on_delete=models.CASCADE)
