from django.db import models

from user.models import HealthProfessional
from constants import MAX_NAME, MAX_DESCRIPTION


class CustomRecommendation(models.Model):
    health_professional = models.ForeignKey(HealthProfessional)
    name = models.CharField(max_length=MAX_NAME)
    recommendation = models.CharField(max_length=MAX_DESCRIPTION)
