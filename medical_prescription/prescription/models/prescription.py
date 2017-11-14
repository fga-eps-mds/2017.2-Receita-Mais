# Django
from django.db import models

# Django Local
from disease.models import Disease
from user.models import HealthProfessional
from medicine.models import Medicine
from medicine.models import ManipulatedMedicine
from exam.models import DefaultExam
from exam.models import CustomExam


class Prescription(models.Model):
    """
    Prescription base model.
    """
    cid = models.ForeignKey(Disease, null=True, blank=True)
    health_professional = models.ForeignKey(HealthProfessional, related_name='health_professsional',
                                            on_delete=models.CASCADE)

    medicines = models.ManyToManyField(Medicine, through='PrescriptionHasMedicine', related_name='medicines')
    manipulated_medicines = models.ManyToManyField(ManipulatedMedicine, through='PrescriptionHasManipulatedMedicine',
                                                   related_name='manipulated_medicines')
    custom_exams = models.ManyToManyField(CustomExam, through='PrescriptionCustomExam', related_name='custom_exams')
    default_exams = models.ManyToManyField(DefaultExam, through='PrescriptionDefaultExam', related_name='default_exams')
    recommendation_prescription = models.ManyToManyField('Recommendation', through='PrescriptionRecommendation',
                                                         related_name='recommendation_prescription')
    is_favorite = models.BooleanField(default=False)
