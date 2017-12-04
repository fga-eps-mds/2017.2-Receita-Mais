from django.contrib import admin

from .models import CustomRecommendation
from .models import NewRecommendation

admin.site.register(CustomRecommendation)
admin.site.register(NewRecommendation)
