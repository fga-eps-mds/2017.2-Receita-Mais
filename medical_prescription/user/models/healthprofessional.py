# Django
from django.db import models

# Local Django
from .user import User
from user import constants
from .usermanager import UserManager


class HealthProfessional(User):
    class Meta:
        unique_together = (('crm', 'crm_state'),)
        verbose_name = ('health_professional')

    crm = models.CharField(max_length=constants.CRM_LENGTH)
    crm_state = models.CharField(choices=constants.UF_CHOICE, max_length=constants.CRM_STATE_LENGTH, default='DF')

    objects = UserManager()
