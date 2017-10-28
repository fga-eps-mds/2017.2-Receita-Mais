# django
from django import forms
import logging
from django.utils.translation import ugettext_lazy as _

# local django
from user import constants


# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class AddPatientForm(forms.Form):
    """
    Form to reset password User
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control s-form-v4__input g-padding-l-0--xs',
                                                            'placeholder': '* exemplo@exemplo.com'}))

    def clean(self, *args, **kwargs):
        """
        Get patient fields.
        """
        logger.debug("Start clean data in ResetPasswordForm.")

        email = self.cleaned_data.get('email')

        # Verify validations in form.
        self.validator_all(email)

        logger.debug("Exit clean data in ResetPasswordForm.")
        return super(AddPatientForm, self).clean(*args, **kwargs)

    def validator_all(self, email):
        """
        Checks validator in all fields.
        """
        logger.debug("Start validations in AddPatientForm.")

        if email is None:
            raise forms.ValidationError({'email': [_(constants.EMAIL_NONE)]})
        elif len(email) > constants.EMAIL_MAX_LENGTH:
            raise forms.ValidationError({'email': [_(constants.EMAIL_SIZE)]})

        logger.debug("Exit validations in AddPatientForm.")
