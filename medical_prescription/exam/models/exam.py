# Django
from django.db import models

# Local Django
from exam import constants


class Exam(models.Model):
    class Meta:
        unique_together = (('auto_increment_id', 'id_tuss'),)

    is_active = models.BooleanField(default=True)
    auto_increment_id = models.AutoField(primary_key=True)
    id_tuss = models.CharField(max_length=constants.ID_TUSS_MAX_LENGTH)
    description = models.CharField(max_length=constants.DESC_TUSS_MAX_LENGTH, default="")
