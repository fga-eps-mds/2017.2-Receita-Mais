# Django imports.
from django.contrib import admin

# Local Django imports.
from .models import Disease

# Register disease in admin page.
admin.site.register(Disease)
