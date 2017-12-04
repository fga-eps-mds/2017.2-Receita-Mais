# Django
from django.db import models
from recommendation.models import NewRecommendation
from prescription.models import Prescription


class PrescriptionNewRecommendation(models.Model):

    prescription = models.ForeignKey(Prescription)
    recommendation = models.ForeignKey(NewRecommendation)
