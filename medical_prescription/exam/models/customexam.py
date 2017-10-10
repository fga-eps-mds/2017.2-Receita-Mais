# Django
from django.db import models

# Local Django
from exam import constants
from .exam import Exam


class CustomExam(Exam):
    id_tuss = models.CharField(max_length=constants.ID_TUSS_MAX_LENGTH, blank=True)
    description = models.CharField(max_length=constants.DESC_MAX_LENGTH)
