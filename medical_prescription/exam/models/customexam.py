# Django
from django.db import models

# Local Django
from .exam import Exam
from exam import constants


class CustomExam(Exam):
    name = models.CharField(max_length=constants.NAME_MAX_LENGTH, unique=True, default="")
    health_professional_FK = models.ForeignKey("user.HealthProfessional", on_delete=models.CASCADE)
