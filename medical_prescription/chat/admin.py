from django.contrib import admin

from .models import Message, Response, ArchiveMessage
# Register your models here.

admin.site.register(Message)
admin.site.register(Response)
admin.site.register(ArchiveMessage)
