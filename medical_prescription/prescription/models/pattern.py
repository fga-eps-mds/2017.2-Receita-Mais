# Standard
import os

# Django
from django.db import models

# Django Local
from user.models import User
from chat.models.pathfile import UploadToPathAndRename
from prescription import constants


class Pattern(models.Model):
    """
    Prescription PDF base model.
    """
    name = models.CharField(max_length=constants.MAX_LENGTH_NAME)
    user_creator = models.ForeignKey(User, related_name="user_creator")

    font = models.CharField(choices=constants.FONT_CHOICE, max_length=100, default='Times-Roman')
    font_size = models.CharField(choices=constants.FONT_SIZE_CHOICE, max_length=100, default=12)
    pagesize = models.CharField(choices=constants.PAGE_SIZE_CHOICE, max_length=100, default='letter')

    clinic = models.CharField(max_length=constants.MAX_LENGTH_CLINIC)
    header = models.CharField(max_length=constants.MAX_LENGTH_HEADER)
    footer = models.CharField(max_length=constants.MAX_LENGTH_FOOTER)

    logo = models.FileField(upload_to=UploadToPathAndRename(os.path.join('logos', 'files')), blank=True, null=True)
    date = models.DateField(auto_now=True)
