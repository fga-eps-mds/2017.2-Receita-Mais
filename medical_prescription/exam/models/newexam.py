# Django
from django.db import models

# Local Django
from exam import constants


class NewExam(models.Model):
    exam_description = models.CharField(max_length=constants.DESC_TUSS_MAX_LENGTH)
