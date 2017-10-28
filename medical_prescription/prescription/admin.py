from django.contrib import admin

# Register your models here.
from .models import (
                    Prescription,
                    PrescriptionExam,
                    PrescriptionMedicine,
                    PrescriptionHasMedicine,
                    PrescriptionHasManipulatedMedicine
                    )

admin.site.register(Prescription)
admin.site.register(PrescriptionExam)
admin.site.register(PrescriptionMedicine)
admin.site.register(PrescriptionHasMedicine)
admin.site.register(PrescriptionHasManipulatedMedicine)
