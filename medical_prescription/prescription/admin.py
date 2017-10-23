from django.contrib import admin

# Register your models here.
from .models import Prescription, PrescriptionExam

admin.site.register(Prescription)
admin.site.register(PrescriptionExam)
