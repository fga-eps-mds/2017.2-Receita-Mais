# Django
from django.db import models

# Django Local
from medicine.models import (ManipulatedMedicine,
                             Medicine)
from prescription.models import NoPatientPrescription


class PrescriptionMedicine(NoPatientPrescription):
    """
    Medicine associetade to many to many fileds in prescription.
    """
    manipulated_medicines = models.ManyToManyField(ManipulatedMedicine,
                                                   through='PrescriptionHasManipulatedMedicine',
                                                   related_name='manipulated_medicines')

    medicines = models.ManyToManyField(Medicine,
                                       through='PrescriptionHasMedicine',
                                       related_name='medicines')
