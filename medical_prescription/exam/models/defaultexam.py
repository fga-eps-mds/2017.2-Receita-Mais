# Django
from django.db import models

# Local Django
from exam import constants
from exam.models import Exam


class DefaultExam(Exam):
    id_tuss = models.CharField(max_length=constants.ID_TUSS_MAX_LENGTH, unique=True)
