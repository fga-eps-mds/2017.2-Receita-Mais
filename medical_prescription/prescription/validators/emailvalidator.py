# django
from django import forms
from django.utils.translation import ugettext_lazy as _

# local django
from prescription import constants


class EmailValidator():

    '''
    Validating patient email in prescription.
    '''

    def validator_email(self, email):
        if email:
            if len(email) > constants.EMAIL_MAX_LENGTH:
                raise forms.ValidationError({'email': [_(constants.EMAIL_SIZE)]})
            elif len(email) < constants.EMAIL_MIN_LENGTH:
                raise forms.ValidationError({'email': [_(constants.EMAIL_SIZE)]})
