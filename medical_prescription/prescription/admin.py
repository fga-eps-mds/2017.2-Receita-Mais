from django.contrib import admin

# Register your models here.
from .models import Prescription, PrescriptionCustomExam, PrescriptionDefaultExam

admin.site.register(Prescription)
admin.site.register(PrescriptionCustomExam)
admin.site.register(PrescriptionDefaultExam)
