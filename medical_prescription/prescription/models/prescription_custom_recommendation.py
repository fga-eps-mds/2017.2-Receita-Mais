# Django
from django.db import models
from recommendation.models import CustomRecommendation
from prescription.models import Prescription


class PrescriptionCustomRecommendation(models.Model):

    prescription = models.ForeignKey(Prescription)
    recommendation = models.ForeignKey(CustomRecommendation)
