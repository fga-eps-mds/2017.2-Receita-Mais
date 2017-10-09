from django import forms
from django.utils.translation import ugettext_lazy as _

from user.models import HealthProfessional
from user.validators import UserValidator
from user import constants


class HealthProfessionalValidator(UserValidator):
    """
    Validating health professional fields.
    """

    def validator_crm(self, crm, crm_state):
        crm_from_database = HealthProfessional.objects.filter(crm=crm)
        crm_state_from_database = HealthProfessional.objects.filter(crm_state=crm_state)

        # Validating CRM
        if crm is not None and len(crm) != constants.CRM_LENGTH:
            raise forms.ValidationError({'crm': [_(constants.CRM_SIZE)]})
        elif crm_state is not None and len(crm_state) != constants.CRM_STATE_LENGTH:
            raise forms.ValidationError({'crm_state': [_(constants.CRM_STATE_SIZE)]})
        elif crm_from_database.exists() and crm_state_from_database.exists():
            raise forms.ValidationError({'crm_state': [_(constants.CRM_EXIST)]})
        elif not crm.isdigit():
            raise forms.ValidationError({'crm': [_(constants.CRM_FORMAT)]})
