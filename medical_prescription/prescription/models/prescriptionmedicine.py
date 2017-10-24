from django.db import models

from medicine.models import (
                             ManipulatedMedicine,
                             Medicine)
from prescription.models import Prescription


class PrescriptionMedicine(Prescription):
    manipulated_medicines = models.ManyToManyField(ManipulatedMedicine,
                                                   through='PrescriptionHasManipulatedMedicine',
                                                   related_name='manipulated_medicines')

    medicines = models.ManyToManyField(Medicine,
                                       through='PrescriptionHasMedicine',
                                       related_name='medicines')
