# standard library
from datetime import date
import logging

# django
from django import forms
from django.utils.translation import ugettext_lazy as _

# local django
from user.forms import FormattedDateField
from user.models import User
from user.validators import UserValidator
from user import constants

# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class UpdateUserForm(forms.ModelForm):
    """
    Form to update the users.
    """

    date_of_birth = FormattedDateField(initial=date.today)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        # Define model to User.
        model = User
        fields = [
            'name', 'date_of_birth', 'phone', 'sex'
        ]

    def clean(self):
        """
        Get user fields.
        """
        logger.debug("Start clean data in UpdateUserForm.")

        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        date_of_birth = self.cleaned_data.get('date_of_birth')
        self.validator_all(name, phone, password, date_of_birth)

        logger.debug("Exit clean data in UpdateUserForm.")

    def validator_all(self, name, phone, password, date_of_birth):
        """
        Checks validator in all fields.
        """

        logger.debug("Start validations in UpdateUserForm.")

        self.verify_password(password)

        validator = UserValidator()
        validator.validator_name(name)
        validator.validator_password(password, password)
        validator.validator_phone_number(phone)
        validator.validator_date_of_birth(date_of_birth)

        logger.debug("Exit validations in UpdateUserForm.")

    def verify_password(self, password):
        """
        Verifies if the given password matches the one in the database.
        """
        check_password = self.instance.check_password(password)

        if not check_password:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_MATCH)]})
