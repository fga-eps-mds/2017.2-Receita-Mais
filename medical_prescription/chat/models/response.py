from django.db import models

from chat import constants
from user.models import User
from .filetype import CustomFileField


class Response(models.Model):
    """
    Create a Response model in database.
    """

    user_from = models.ForeignKey(User, related_name="user_response_from")
    user_to = models.ForeignKey(User, related_name="user_response_to")

    text = models.CharField(max_length=constants.MAX_LENGTH_TEXT_MESSAGE)
    files = CustomFileField(upload_to='media/', content_types=['application/pdf', 'image/png', 'audio/mpeg', ], max_upload_size=20971520, blank=True, null=True)

    date = models.DateField(auto_now=True)
