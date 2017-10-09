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
