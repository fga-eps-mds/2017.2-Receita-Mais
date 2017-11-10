import os
import hashlib
import random

from django.db import models

from chat import constants
from user.models import User

from uuid import uuid4


def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            hashname = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, hashname, filename)
    return wrapper


class Response(models.Model):
    """
    Create a Response model in database.
    """

    user_from = models.ForeignKey(User, related_name="user_response_from")
    user_to = models.ForeignKey(User, related_name="user_response_to")

    text = models.CharField(max_length=constants.MAX_LENGTH_TEXT_MESSAGE)
    files = models.FileField(upload_to=path_and_rename('upload/media/'), blank=True, null=True)

    date = models.DateField(auto_now=True)
