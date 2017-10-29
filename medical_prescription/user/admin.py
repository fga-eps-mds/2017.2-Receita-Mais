# Django
from django.contrib import admin
from .models import (
    User, HealthProfessional, Patient, UserActivateProfile, ResetPasswordProfile,
    SendInvitationProfile, AssociatedHealthProfessionalAndPatient,
)


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active']


admin.site.register(User, UserAdmin)
admin.site.register(HealthProfessional)
admin.site.register(Patient)
admin.site.register(UserActivateProfile)
admin.site.register(ResetPasswordProfile)
admin.site.register(SendInvitationProfile)
admin.site.register(AssociatedHealthProfessionalAndPatient)
