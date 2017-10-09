from datetime import date

from django import forms
from django.utils.translation import ugettext_lazy as _

from user import constants
from user.forms import FormattedDateField
from user.models import User


class UpdateUserForm(forms.ModelForm):

    # It verifies if the given password matches the one in the database.
    def verify_password(self, password):
        return self.instance.check_password(password)

    date_of_birth = FormattedDateField(initial=date.today)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'name', 'date_of_birth', 'phone', 'sex'
        ]

    def clean(self):
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        date_of_birth = self.cleaned_data.get('date_of_birth')

        today = date.today()

        # Validating date of birth Format.
        try:
            born = today.year - date_of_birth.year - \
                ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        except:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_FORMAT)]})

        # Validating password.
        if len(password) < constants.PASSWORD_MIN_LENGTH:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_SIZE)]})
        elif len(password) > constants.PASSWORD_MAX_LENGTH:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_SIZE)]})
        elif not password.isalnum():
            raise forms.ValidationError({'password': [_(constants.PASSWORD_FORMAT)]})
        elif not self.verify_password(password):
            raise forms.ValidationError({'password': [_(constants.PASSWORD_MATCH)]})

        # Validating name.
        elif name is not None and len(name) > constants.NAME_MAX_LENGHT:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif name is not None and len(name) < constants.NAME_MIN_LENGTH:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif name is not None and not all(x.isalpha() or x.isspace() for x in name):
            raise forms.ValidationError({'name': [_(constants.NAME_FORMAT)]})

        # Validating phone number.
        elif phone is not None and len(phone) > constants.PHONE_NUMBER_FIELD_LENGTH_MAX:
            raise forms.ValidationError({'phone': [_(constants.PHONE_NUMBER_SIZE)]})
        elif phone is not None and len(phone) < constants.PHONE_NUMBER_FIELD_LENGTH_MIN:
            raise forms.ValidationError({'phone': [_(constants.PHONE_NUMBER_SIZE)]})
        elif phone is not None and not phone.isdigit():
            raise forms.ValidationError({'phone': [_(constants.PHONE_NUMBER_FORMAT)]})

        # Validating date of birth.
        elif born < constants.DATE_OF_BIRTH_MIN_PATIENT:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_MIN_PATIENT_ERROR)]})
