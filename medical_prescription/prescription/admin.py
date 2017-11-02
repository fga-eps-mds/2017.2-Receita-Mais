from django.contrib import admin

# Register your models here.
from .models import (
                    Prescription,
                    PrescriptionCustomExam,
                    PrescriptionDefaultExam,
                    PrescriptionMedicine,
                    PrescriptionHasMedicine,
                    PrescriptionHasManipulatedMedicine,
                    PrescriptionRecommendation,
                    )

admin.site.register(Prescription)
admin.site.register(PrescriptionMedicine)
admin.site.register(PrescriptionHasMedicine)
admin.site.register(PrescriptionHasManipulatedMedicine)
admin.site.register(PrescriptionRecommendation)
admin.site.register(PrescriptionCustomExam)
admin.site.register(PrescriptionDefaultExam)
