# standard library
from datetime import date
import logging

# django
from django import forms
from django.utils.translation import ugettext_lazy as _

# local django
from user.models import HealthProfessional
from user.validators import UserValidator
from user import constants

# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class HealthProfessionalValidator(UserValidator):
    """
    Validating health professional fields.
    """

    def validator_crm(self, crm, crm_state):
        """
        Validating crm.
        """
        logger.debug("Start validator_crm.")

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

        logger.debug("Exit validator_crm.")

    def validartor_specialty(self, specialty_first, specialty_second):
        """
        Validating specialty.
        """
        logger.debug("Start validartor_specialty.")
        if specialty_first is not None and len(specialty_first) < constants.SPECIALITY_MIN_LENGTH:
            raise forms.ValidationError({'specialty_first': [_(constants.SPECIALITY_SIZE)]})
        elif specialty_first == 'Nao Possui':
            raise forms.ValidationError({'specialty_first': [_(constants.SPECIALITY_REQUIRED)]})
        if specialty_second is not None and len(specialty_second) < constants.SPECIALITY_MIN_LENGTH:
            raise forms.ValidationError({'specialty_second': [_(constants.SPECIALITY_SIZE)]})
            logger.debug("Exit validartor_specialty.")

    def validator_date_of_birth(self, date_of_birth):
        """
        Validating date of birth.
        """
        logger.debug("Start validator_date_of_birth.")

        today = date.today()
        try:
            born = today.year - date_of_birth.year - \
                ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        except:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_FORMAT)]})

        # Checks if health professional is under 18.
        if born < constants.DATE_OF_BIRTH_MIN:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_MIN_ERROR)]})

        logger.debug("Exit validator_date_of_birth.")
