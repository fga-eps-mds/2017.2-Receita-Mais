# Django
from django.db import models

# Local Django
from .exam import Exam


class CustomExam(Exam):
    health_professional_FK = models.ForeignKey("user.HealthProfessional", on_delete=models.CASCADE)
