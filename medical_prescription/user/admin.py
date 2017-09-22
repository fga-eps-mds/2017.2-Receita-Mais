<<<<<<< HEAD
=======
from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active']


admin.site.register(User, UserAdmin)
>>>>>>> 42b3c2eb1d8f1ff6864b649d12cab467b262fa3b
