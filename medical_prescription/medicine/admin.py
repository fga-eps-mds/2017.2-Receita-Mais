from django.contrib import admin
from medicine.models import ActivePrinciple
from medicine.models import CustomActivePrinciple

admin.site.register(ActivePrinciple)
admin.site.register(CustomActivePrinciple)
