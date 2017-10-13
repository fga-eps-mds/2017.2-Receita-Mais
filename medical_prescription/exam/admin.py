from django.contrib import admin

from .models import Exam, CustomExam
# Register your models here.

admin.site.register(Exam)
admin.site.register(CustomExam)
