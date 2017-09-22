# Django
from django.contrib import admin

# Django Local
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active']


admin.site.register(User, UserAdmin)
