# Django
from django.db import models

# Local Django
from exam import constants


class Exam(models.Model):
    is_active = models.BooleanField(default=True)
    id_tuss = models.CharField(max_length=constants.ID_TUSS_MAX_LENGTH, unique=True)
    description = models.CharField(max_length=constants.DESC_TUSS_MAX_LENGTH)
