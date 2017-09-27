# Django
from django.contrib import admin
from .models import (
    User, HealthProfessional, Patient
)


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active']


admin.site.register(User, UserAdmin)
admin.site.register(HealthProfessional)
admin.site.register(Patient)
