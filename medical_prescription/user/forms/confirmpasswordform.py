# standard library
import logging

# django
from django import forms

# local django
from user import constants
from user.validators import UserValidator

# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class ConfirmPasswordForm(forms.Form):
    """
    Form to confirm password.
    """

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'type': 'password'}),
                               label='')

    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                       'type': 'password'}),
                                            label='')

    def clean(self, *args, **kwargs):
        logger.debug("Start clean data in ConfirmPasswordForm.")
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        validator = UserValidator()

        validator.validator_password(password, password_confirmation)

        logger.debug("Exit clean data in ConfirmPasswordForm.")
        return super(ConfirmPasswordForm, self).clean(*args, **kwargs)
