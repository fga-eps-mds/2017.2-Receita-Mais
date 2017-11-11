import os
import hashlib
import random

from django.db import models

from chat import constants
from user.models import User

from uuid import uuid4
from django.utils.deconstruct import deconstructible


@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]

        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        hashname = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
        # return the whole path to the file
        return os.path.join(self.sub_path, hashname, filename)


class Response(models.Model):
    """
    Create a Response model in database.
    """

    user_from = models.ForeignKey(User, related_name="user_response_from")
    user_to = models.ForeignKey(User, related_name="user_response_to")

    text = models.CharField(max_length=constants.MAX_LENGTH_TEXT_MESSAGE)
    files = models.FileField(upload_to=UploadToPathAndRename(os.path.join('upload', 'files')), blank=True, null=True)

    date = models.DateField(auto_now=True)
