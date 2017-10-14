# standard library
import logging

# django
from django import forms

# local django
from user import constants

# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class ConfirmPasswordForm(forms.Form):
    """
    Form to confirm password.
    """

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}),
                               label='')
    password_confirmation = forms.CharField(widget=forms.PasswordInput(
                            attrs={'placehold': 'password confirmation'}),
                            label='')

    def clean(self, *args, **kwargs):
        logger.debug("Start clean data in ConfirmPasswordForm.")
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if(password != password_confirmation):
            raise forms.ValidationError('As senhas devem ser iguais')
        else:
            # Nothing to do.
            pass

        logger.debug("Exit clean data in ConfirmPasswordForm.")
        return super(ConfirmPasswordForm, self).clean(*args, **kwargs)
