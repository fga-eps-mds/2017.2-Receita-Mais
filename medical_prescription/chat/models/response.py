import os

# Django
from django.db import models

# Django Local
from chat import constants
from user.models import User
from .pathfile import UploadToPathAndRename


class Response(models.Model):
    """
    Create a Response model in database.
    """

    user_from = models.ForeignKey(User, related_name="user_response_from")
    user_to = models.ForeignKey(User, related_name="user_response_to")

    text = models.CharField(max_length=constants.MAX_LENGTH_TEXT_MESSAGE)
    files = models.FileField(upload_to=UploadToPathAndRename(os.path.join('upload', 'files')), blank=True, null=True)
    file_name = models.CharField(max_length=300, blank=True)

    date = models.DateField(auto_now=True)

    as_read = models.BooleanField(default=False)
