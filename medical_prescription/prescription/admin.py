from django.contrib import admin

# Register your models here.
from .models import (
                    Prescription,
                    PrescriptionCustomExam,
                    PrescriptionDefaultExam,
                    PrescriptionHasMedicine,
                    PrescriptionHasManipulatedMedicine,
                    PrescriptionNewExam,
                    PrescriptionNewRecommendation,
                    NoPatientPrescription,
                    PatientPrescription,
                    Pattern
                    )

admin.site.register(Prescription)
admin.site.register(PrescriptionHasMedicine)
admin.site.register(PrescriptionHasManipulatedMedicine)
admin.site.register(PrescriptionCustomExam)
admin.site.register(PrescriptionDefaultExam)
admin.site.register(PrescriptionNewExam)
admin.site.register(PrescriptionNewRecommendation)
admin.site.register(PatientPrescription)
admin.site.register(NoPatientPrescription)
admin.site.register(Pattern)
