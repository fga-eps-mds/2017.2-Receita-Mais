# standard library
from datetime import date

# django
from django import forms
from django.utils.translation import ugettext_lazy as _

# local django
from user.models import HealthProfessional
from user.validators import UserValidator
from user import constants


class HealthProfessionalValidator(UserValidator):
    """
    Validating health professional fields.
    """

    def validator_crm(self, crm, crm_state):
        """
        Validating crm.
        """

        crm_from_database = HealthProfessional.objects.filter(crm=crm)
        crm_state_from_database = HealthProfessional.objects.filter(crm_state=crm_state)

        if crm is not None and len(crm) != constants.CRM_LENGTH:
            raise forms.ValidationError({'crm': [_(constants.CRM_SIZE)]})
        elif crm_state is not None and len(crm_state) != constants.CRM_STATE_LENGTH:
            raise forms.ValidationError({'crm_state': [_(constants.CRM_STATE_SIZE)]})
        elif crm_from_database.exists() and crm_state_from_database.exists():
            raise forms.ValidationError({'crm_state': [_(constants.CRM_EXIST)]})
        elif not crm.isdigit():
            raise forms.ValidationError({'crm': [_(constants.CRM_FORMAT)]})

    def validator_date_of_birth(self, date_of_birth):
        """
        Validating date of birth.
        """

        today = date.today()
        try:
            born = today.year - date_of_birth.year - \
                ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        except:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_FORMAT)]})

        # Checks if health professional is under 18.
        if born < constants.DATE_OF_BIRTH_MIN:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_MIN_ERROR)]})
