from django.contrib import admin

from .models import DefaultExam, CustomExam, Exam
# Register your models here.

admin.site.register(Exam)
admin.site.register(DefaultExam)
admin.site.register(CustomExam)
