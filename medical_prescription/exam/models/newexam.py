# Django
from django.db import models

# Local Django


class NewExam(models.Model):
    exam_description = models.CharField(max_length=100)
