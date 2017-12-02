# standard library
import logging

# django
from django import forms

# local django
from user.models import Patient
from user.forms import UserForm
from user.validators import PatientValidator
from user import constants


# LocalFlavor
from localflavor.br.forms import BRCPFField


# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class PatientForm(UserForm):
    """
    Form to register patientl.
    """

    email = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'form-control s-form-v4__input'}), required=False)

    CPF_document = BRCPFField(max_length=14, min_length=11,
                              widget=forms.TextInput(attrs={'class': 'form-control s-form-v4__input',
                                                            'placeholder': '* 12345678911'}))

    CEP = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v4__input',
                                                        'placeholder': '* 12345678'}))

    UF = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v4__input',
                                                       'placeholder': '* DF'}))

    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v4__input',
                                                         'placeholder': '* Brasília'}))

    neighborhood = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v4__input',
                                                                 'placeholder': '* Asa Norte'}))

    complement = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v4__input',
                                                               'size': 200,
                                                               'placeholder': '* Qd 70, Lt 8 Casa 2'}))

    class Meta:
        # Define model to patient.
        model = Patient
        fields = [
                'name', 'email', 'date_of_birth', 'phone', 'sex',
                'CPF_document', 'password', 'CEP', 'UF', 'city', 'neighborhood',
                'complement'
                ]

    def clean(self):
        """
        Get patient fields.
        """
        logger.debug("Start clean data in PatientForm.")

        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('confirm_password')
        date_of_birth = self.cleaned_data.get('date_of_birth')

        # Verify validations in form.
        self.validator_all(name, phone, password, password_confirmation, date_of_birth)
        logger.debug("Exit clean data in PatientForm.")

    def validator_all(self, name, phone, password, password_confirmation, date_of_birth):
        """
        Checks validator in all fields.
        """

        logger.debug("Start validations in PatientForm.")
        validator = PatientValidator()

        # Fields common all users.
        validator.validator_password(password, password_confirmation)
        validator.validator_name(name)
        validator.validator_phone_number(phone)
        validator.validator_date_of_birth(date_of_birth)
