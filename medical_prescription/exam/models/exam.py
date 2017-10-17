# Django
from django.db import models

# Local Django
from exam import constants


class Exam(models.Model):
    is_active = models.BooleanField(default=True)
    auto_increment_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=constants.DESC_TUSS_MAX_LENGTH, default="")
