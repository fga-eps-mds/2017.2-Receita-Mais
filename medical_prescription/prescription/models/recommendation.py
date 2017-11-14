# Django
from django.db import models


class Recommendation(models.Model):
    """
    Model to create a recommendation.
    """
    recommendation = models.CharField(max_length=1000)
