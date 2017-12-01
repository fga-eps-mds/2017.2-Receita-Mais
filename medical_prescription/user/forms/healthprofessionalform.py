# standard library
import logging

# django
from django import forms

# local django
from user.models import HealthProfessional
from user.forms import UserForm
from user import constants
from user.validators import HealthProfessionalValidator

# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class HealthProfessionalForm(UserForm):
    """
    Form to register health professional.
    """
    list_main_specialty = constants.SPECIALITY_CHOICE.copy()
    del list_main_specialty[0]
    crm = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v4__input',
                                                        'placeholder': '* 00000'}))
    crm_state = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control s-form-v4__input',
                                                             'placeholder': '* Crm'}), choices=constants.UF_CHOICE)
    specialty_first = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control s-form-v4__input',
                                                                   'placeholder': '* Crm'}),
                                        choices=list_main_specialty)
    specialty_second = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control s-form-v4__input',
                                                                    'placeholder': '* Crm'}),
                                         choices=constants.SPECIALITY_CHOICE)

    class Meta:
        # Define model to form.
        model = HealthProfessional
        fields = ('name', 'email', 'date_of_birth', 'phone', 'sex', 'crm', 'crm_state', 'password',
                  'specialty_first', 'specialty_second')

    def clean(self):
        """
        Get health professional fields.
        """
        logger.debug("Start clean data in HealthProfessionalForm.")

        crm = self.cleaned_data.get('crm')
        crm_state = self.cleaned_data.get('crm_state')
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('confirm_password')
        date_of_birth = self.cleaned_data.get('date_of_birth')
        specialty_first = self.cleaned_data.get('specialty_first')
        specialty_second = self.cleaned_data.get('specialty_second')

        # Verify validations in form.
        self.validator_all(name, phone, email, password, password_confirmation, crm, crm_state, date_of_birth,
                           specialty_first, specialty_second)
        logger.debug("Exit clean data in HealthProfessionalForm.")

    def validator_all(self, name, phone, email, password, password_confirmation, crm, crm_state, date_of_birth,
                      specialty_first, specialty_second):
        """
        Checks validator in all fields.
        """

        logger.debug("Start validations in HealthProfessionalForm.")
        validator = HealthProfessionalValidator()

        # Fields common all users.
        validator.validator_email(email)
        validator.validator_password(password, password_confirmation)
        validator.validator_name(name)
        validator.validator_phone_number(phone)
        validator.validator_date_of_birth(date_of_birth)

        # Fields specify to the health professional.
        validator.validator_crm(crm, crm_state)
        validator.validartor_specialty(specialty_first, specialty_second)
        logger.debug("Exit validations in HealthProfessionalForm.")
