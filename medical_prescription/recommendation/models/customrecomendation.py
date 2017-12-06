from django.db import models

from user.models import HealthProfessional
from recommendation.constants import MAX_NAME, MAX_DESCRIPTION


class CustomRecommendation(models.Model):
    class Meta:
        unique_together = (('name', 'health_professional'),)

    name = models.CharField(max_length=MAX_NAME, unique=True, default="")
    recommendation = models.CharField(max_length=MAX_DESCRIPTION)
    health_professional = models.ForeignKey(HealthProfessional)
    is_active = models.BooleanField(default=False)
    auto_increment_id = models.AutoField(primary_key=True)
