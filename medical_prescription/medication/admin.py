# django
from django.contrib import admin

# local django
from .models import (Medicine,
                     ManipulatedMedicine)

admin.site.register(Medicine)
admin.site.register(ManipulatedMedicine)
