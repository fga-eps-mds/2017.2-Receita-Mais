from django.contrib import admin

from .models import (Medicine,
                     ManipulatedMedicine,
                     ActivePrinciple,
                     CustomActivePrinciple)

admin.site.register(Medicine)
admin.site.register(ManipulatedMedicine)
admin.site.register(ActivePrinciple)
admin.site.register(CustomActivePrinciple)
