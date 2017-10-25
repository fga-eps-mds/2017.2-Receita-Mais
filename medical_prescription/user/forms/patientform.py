# standard library
from datetime import date
import logging

# django
from django import forms

# local django
from user.models import Patient
from user.forms import (UserForm,
                        FormattedDateField
                        )
from user.validators import PatientValidator
from user import constants


# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class PatientForm(UserForm):
    """
    Form to register patientl.
    """
    id_document = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v3__input',
                                                                'placeholder': '* 00000'}))
    date_of_birth = FormattedDateField(initial=date.today)

    class Meta:
        # Define model to patient.
        model = Patient
        fields = [
                'name', 'email', 'date_of_birth', 'phone', 'sex',
                'id_document', 'password'
                ]

    def clean(self):
        """
        Get patient fields.
        """
        logger.debug("Start clean data in PatientForm.")

        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('confirm_password')
        id_document = self.cleaned_data.get('id_document')
        date_of_birth = self.cleaned_data.get('date_of_birth')

        # Verify validations in form.
        self.validator_all(name, phone, email, password, password_confirmation, id_document, date_of_birth)
        logger.debug("Exit clean data in PatientForm.")

    def validator_all(self, name, phone, email, password, password_confirmation, id_document, date_of_birth):
        """
        Checks validator in all fields.
        """

        logger.debug("Start validations in PatientForm.")
        validator = PatientValidator()

        # Fields common all users.
        # validator.validator_email(email)
        validator.validator_password(password, password_confirmation)
        validator.validator_name(name)
        validator.validator_phone_number(phone)
        validator.validator_date_of_birth(date_of_birth)

        # Fields specify to the patient.
        validator.validator_document(id_document)
        logger.debug("Exit validations in PatientForm.")
