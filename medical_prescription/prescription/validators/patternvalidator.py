# django
from django import forms
from django.utils.translation import ugettext_lazy as _

# local django
from prescription import constants


class PatternValidator():
    """
    Validating custom Message and Response fields.
    """

    # Validating name.
    def validator_name(self, name):
        if name is not None and len(name) > constants.MAX_LENGTH_NAME:
            raise forms.ValidationError({'name': [_(constants.LENGTH_NAME)]})

    # Validanting clinic.
    def validator_clinic(self, clinic):
        if clinic is not None and len(clinic) > constants.MAX_LENGTH_CLINIC:
            raise forms.ValidationError({'clinic': [_(constants.LENGTH_CLINIC)]})

    # Validanting header.
    def validator_header(self, header):
        if header is not None and len(header) > constants.MAX_LENGTH_HEADER:
            raise forms.ValidationError({'header': [_(constants.LENGTH_HEADER)]})

    # Validanting footer.
    def validator_footer(self, footer):
        if footer is not None and len(footer) > constants.MAX_LENGTH_FOOTER:
            raise forms.ValidationError({'footer': [_(constants.LENGTH_FOOTER)]})

    # Validanting file.
    def validator_file(self, content):
        content_type = content.content_type.split('/')[1]
        if content_type in constants.CONTENT_TYPES:
            if content._size > constants.MAX_UPLOAD_SIZE:
                raise forms.ValidationError({'logo': [_(constants.FILE_SIZE)]})
        else:
            raise forms.ValidationError({'logo': [_(constants.FORMAT_ERROR)]})
