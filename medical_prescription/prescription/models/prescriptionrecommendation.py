# Django
from django.db import models


class PrescriptionRecommendation(models.Model):
    """
    Model to associate prescription to recommendation many to many cardinality.
    """
    prescription = models.ForeignKey('Prescription')
    recommendation = models.ForeignKey('Recommendation')
