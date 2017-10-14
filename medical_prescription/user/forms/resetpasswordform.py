# django
from django import forms
import logging

# local django
from user.validators import UserValidator
from user import constants


# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class ResetPasswordForm(forms.Form):
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
        return super(ResetPasswordForm, self).clean(*args, **kwargs)

    def validator_all(self, email):
        """
        Checks validator in all fields.
        """
        logger.debug("Start validations in ResetPasswordForm.")

        validator = UserValidator()
        validator.validator_email_in_reset_password(email)

        logger.debug("Exit validations in ResetPasswordForm.")
