from django.contrib import admin

from .models import Message, Response
# Register your models here.

admin.site.register(Message)
admin.site.register(Response)
