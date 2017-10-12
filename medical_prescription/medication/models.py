from django.db import models
from medication import constants
from user.models import HealthProfessional


class Medication(models.Model):

    name = models.CharField(max_length=constants.MAX_LENGHT_NAME,
                            blank=False,
                            default=constants.DEFAULT_NAME)

    active_ingredient = models.CharField(max_length=constants.MAX_LENGHT_NAME,
                                         blank=False,
                                         default=constants.DEFAULT_NAME)

    laboratory = models.CharField(max_length=constants.MAX_LENGHT_NAME,
                                  blank=False,
                                  default=constants.DEFAULT_NAME)

    description = models.TextField()
    is_restricted = models.BooleanField(default=False)
    health_professional = models.ForeignKey(HealthProfessional)
