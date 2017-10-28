# django
from django.db import models

# local django
from medicine import constants
from user.models import HealthProfessional


class ManipulatedMedicine(models.Model):
    recipe_name = models.CharField(max_length=constants.MAX_LENGTH_NAME,
                                   blank=False)

    physical_form = models.CharField(max_length=constants.MAX_LENGTH_PHYSICAL_FORM,
                                     blank=False)

    quantity = models.FloatField(default=constants.DEFAULT_QUANTITY, blank=False)
    measurement = models.CharField(max_length=constants.MAX_LENGTH_MEASUREMENT)
    composition = models.TextField()

    health_professional = models.ForeignKey(HealthProfessional)
