# Django
from django.db import models

# Django Local
from disease.models import Disease
from user.models import HealthProfessional
from medicine.models import Medicine
from medicine.models import ManipulatedMedicine
from exam.models import DefaultExam
from exam.models import CustomExam
from exam.models import NewExam
from recommendation.models import NewRecommendation, CustomRecommendation


class Prescription(models.Model):
    """
    Prescription base model.
    """
    cid = models.ForeignKey(Disease, null=True, blank=True)
    health_professional = models.ForeignKey(HealthProfessional, related_name='health_professsional',
                                            on_delete=models.CASCADE)

    date = models.DateTimeField(blank=True, auto_now_add=True)

    medicines = models.ManyToManyField(Medicine, through='PrescriptionHasMedicine', related_name='medicines')

    manipulated_medicines = models.ManyToManyField(ManipulatedMedicine, through='PrescriptionHasManipulatedMedicine',
                                                   related_name='manipulated_medicines')

    custom_exams = models.ManyToManyField(CustomExam, through='PrescriptionCustomExam',
                                          related_name='custom_exams')

    default_exams = models.ManyToManyField(DefaultExam, through='PrescriptionDefaultExam',
                                           related_name='default_exams')

    new_exams = models.ManyToManyField(NewExam, through='PrescriptionNewExam',
                                       related_name='new_exams')

    new_recommendations = models.ManyToManyField(NewRecommendation, through='PrescriptionNewRecommendation',
                                                 related_name='new_recommendations')

    custom_recommendations = models.ManyToManyField(CustomRecommendation, through='PrescriptionCustomRecommendation',
                                                 related_name='custom_recommendations')

    is_favorite = models.BooleanField(default=False)
