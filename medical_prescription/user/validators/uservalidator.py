# standard library
from datetime import date
import logging

# django
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# local django
from user import constants
from user.models import User

# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class UserValidator():
    """
    Validating user fields.
    """

    def validator_email(self, email):
        """
        Validating email.
        """
        logger.debug("Start validator_email.")

        email_from_database = User.objects.filter(email=email)

        if email_from_database.exists():
            raise ValidationError({'email': [_(constants.EMAIL_EXISTS)]})
        elif email is None:
            raise forms.ValidationError({'email': [_(constants.EMAIL_NONE)]})
        elif len(email) > constants.EMAIL_MAX_LENGTH:
            raise forms.ValidationError({'email': [_(constants.EMAIL_SIZE)]})

        logger.debug("Exit validator_email.")

    def validator_email_in_reset_password(self, email):
        """
        Validating email.
        """
        logger.debug("Start validator_email_in_reset_password.")

        email_from_database = User.objects.filter(email=email)

        if email_from_database.exists():
            pass
        else:
            pass

        logger.debug("Exit validator_email_in_reset_password.")

    def validator_password(self, password, password_confirmation):
        """
        Validating password.
        """

        logger.debug("Start validator_password.")

        if len(password) < constants.PASSWORD_MIN_LENGTH:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_SIZE)]})
        elif len(password) > constants.PASSWORD_MAX_LENGTH:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_SIZE)]})
        elif not password.isalnum():
            raise forms.ValidationError({'password': [_(constants.PASSWORD_FORMAT)]})
        elif password != password_confirmation:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_MATCH)]})

        logger.debug("Exit validator_password.")

    def validator_name(self, name):
        """
        Validating name.
        """
        logger.debug("Start validator_name.")

        if name is not None and len(name) > constants.NAME_MAX_LENGHT:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif name is not None and len(name) < constants.NAME_MIN_LENGTH:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif name is not None and not all(x.isalpha() or x.isspace() for x in name):
            raise forms.ValidationError({'name': [_(constants.NAME_FORMAT)]})

        logger.debug("Exit validator_name.")

    def validator_phone_number(self, phone):
        """
        Validating phone number.
        """
        logger.debug("Start validator_phone_number.")

        if phone is None:
            raise forms.ValidationError({'phone': [_(constants.PHONE_NULL)]})
        elif len(phone) < constants.PHONE_NUMBER_FIELD_LENGTH_MIN:
            raise forms.ValidationError({'phone': [_(constants.PHONE_NUMBER_SIZE)]})

        logger.debug("Exit validator_phone_number.")

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

        if born < constants.DATE_OF_BIRTH_MIN_PATIENT:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_MIN_PATIENT_ERROR)]})

        logger.debug("Exit validator_date_of_birth.")
