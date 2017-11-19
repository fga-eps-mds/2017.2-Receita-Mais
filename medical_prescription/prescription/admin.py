from django.contrib import admin

# Register your models here.
from .models import (
                    Prescription,
                    PrescriptionCustomExam,
                    PrescriptionDefaultExam,
                    PrescriptionHasMedicine,
                    PrescriptionHasManipulatedMedicine,
                    PrescriptionRecommendation,
                    NoPatientPrescription,
                    PatientPrescription,
                    Recommendation,
                    Pattern
                    )

admin.site.register(Prescription)
admin.site.register(PrescriptionHasMedicine)
admin.site.register(PrescriptionHasManipulatedMedicine)
admin.site.register(PrescriptionRecommendation)
admin.site.register(PrescriptionCustomExam)
admin.site.register(PrescriptionDefaultExam)
admin.site.register(PatientPrescription)
admin.site.register(NoPatientPrescription)
admin.site.register(Recommendation)
admin.site.register(Pattern)
