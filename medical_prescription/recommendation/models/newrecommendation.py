# Django
from django.db import models

# Local Django


class NewRecommendation(models.Model):
    recommendation_description = models.CharField(max_length=250)
