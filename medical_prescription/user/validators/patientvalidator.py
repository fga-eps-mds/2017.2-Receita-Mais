from datetime import date

from django import forms
from django.utils.translation import ugettext_lazy as _

from user.validators import UserValidator
from user import constants


class PatientValidator(UserValidator):
    """
    Validating patient fields.
    """

    def validator_document(self, id_document):
        """
        Validating id document.
        """
        if id_document is not None and len(id_document) < constants.ID_DOCUMENT_MIN_LENGTH:
            raise forms.ValidationError({'id_document': [_(constants.ID_DOCUMENT_SIZE)]})
        elif id_document is not None and len(id_document) > constants.ID_DOCUMENT_MAX_LENGTH:
            raise forms.ValidationError({'id_document': [_(constants.ID_DOCUMENT_SIZE)]})
        elif not id_document.isdigit():
            raise forms.ValidationError({'id_document': [_(constants.ID_DOCUMENT_FORMAT)]})

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

        if born < constants.DATE_OF_BIRTH_MIN_PATIENT:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_MIN_PATIENT_ERROR)]})
