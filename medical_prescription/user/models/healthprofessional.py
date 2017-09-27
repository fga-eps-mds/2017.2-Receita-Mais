# Django
from django.db import models

# Local Django
from .user import User
from user import constants
from .usermanager import UserManager


class HealthProfessional(User):
    crm = models.CharField(max_length=constants.CRM_LENGTH, unique=True)
    crm_state = models.CharField(choices=constants.UF_CHOICE, max_length=constants.CRM_STATE_LENGTH, default='DF')

    objects = UserManager()
