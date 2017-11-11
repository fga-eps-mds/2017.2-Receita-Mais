import os
import hashlib
import random

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
