from django.db import models
from medication import constants
from user.models import HealthProfessional


class Medicine(models.Model):

    name = models.CharField(max_length=constants.MAX_LENGHT_NAME,
                            blank=False,
                            default=constants.DEFAULT_NAME)

    active_ingredient = models.CharField(max_length=constants.MAX_LENGHT_NAME,
                                         blank=False,
                                         default=constants.DEFAULT_NAME)

    laboratory = models.CharField(max_length=constants.MAX_LENGTH_NAME,
                                  blank=False,
                                  default=constants.DEFAULT_NAME)

    description = models.TextField()
    is_restricted = models.BooleanField(default=False)


class ManipulatedMedicine(models.Model):
    recipe_name = models.CharField(max_length=constants.MAX_LENGHT_NAME,
                                   blank=False)

    physical_form = models.CharField(max_length=constants.MAX_LENGTH_PHYSICAL_FORM,
                                     blank=False)

    quantity = models.FloatField(default=constants.DEFAULT_QUANTITY, blank=False)
    measurement = models.charField(max_length=constants.MAX_LENGTH_MEASUREMENT)
    composition = models.TextField()

    health_professional = models.ForeignKey(HealthProfessional)
