# django
from django.db import models

# local django
from medicine import constants


class Medicine(models.Model):

    name = models.CharField(max_length=constants.MAX_LENGTH_NAME,
                            blank=False,
                            default=constants.DEFAULT_NAME)

    active_ingredient = models.CharField(max_length=constants.MAX_LENGTH_NAME,
                                         blank=False,
                                         default=constants.DEFAULT_NAME)

    laboratory = models.CharField(max_length=constants.MAX_LENGTH_NAME,
                                  blank=False,
                                  default=constants.DEFAULT_NAME)

    description = models.TextField()
    is_restricted = models.BooleanField(default=False)
