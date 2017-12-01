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

    list_main_specialty = constants.SPECIALITY_CHOICE.copy()
    del list_main_specialty[0]
    crm = models.CharField(max_length=constants.CRM_LENGTH)
    crm_state = models.CharField(choices=constants.UF_CHOICE, max_length=constants.CRM_STATE_LENGTH, default='DF')
    specialty_first = models.CharField(choices=list_main_specialty,
                                       max_length=constants.SPECIALITY_LENGTH)
    specialty_second = models.CharField(choices=constants.SPECIALITY_CHOICE, max_length=constants.SPECIALITY_LENGTH,
                                        default='Nao Possui')

    objects = UserManager()
