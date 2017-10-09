from datetime import date

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from user.models import HealthProfessional, User
from user.forms import UserForm
from user import constants


class HealthProfessionalForm(UserForm):
    crm = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v3__input',
                                                        'placeholder': '* 00000'}))
    crm_state = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control s-form-v3__input',
                                                             'placeholder': '* Crm'}), choices=constants.UF_CHOICE)

    class Meta:
        model = HealthProfessional
        fields = ('name', 'email', 'date_of_birth', 'phone', 'sex', 'crm', 'crm_state', 'password',)

    def clean(self):
        crm = self.cleaned_data.get('crm')
        crm_state = self.cleaned_data.get('crm_state')
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('confirm_password')
        date_of_birth = self.cleaned_data.get('date_of_birth')

        email_from_database = User.objects.filter(email=email)

        # Validating date of birth Format.
        today = date.today()
        try:
            born = today.year - date_of_birth.year - \
                ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        except:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_FORMAT)]})

        crm_from_database = HealthProfessional.objects.filter(crm=crm)
        crm_state_from_database = HealthProfessional.objects.filter(crm_state=crm_state)

        # Validating CRM
        if crm is not None and len(crm) != constants.CRM_LENGTH:
            raise forms.ValidationError({'crm': [_(constants.CRM_SIZE)]})
        elif crm_state is not None and len(crm_state) != constants.CRM_STATE_LENGTH:
            raise forms.ValidationError({'crm_state': [_(constants.CRM_STATE_SIZE)]})
        elif crm_from_database.exists() and crm_state_from_database.exists():
            raise forms.ValidationError({'crm_state': [_(constants.CRM_EXIST)]})
        elif not crm.isdigit():
            raise forms.ValidationError({'crm': [_(constants.CRM_FORMAT)]})

        # Validating email
        elif email_from_database.exists():
            raise ValidationError({'email': [_(constants.EMAIL_EXISTS)]})
        elif email is None:
            raise forms.ValidationError({'email': [_(constants.EMAIL_NONE)]})
        elif len(email) > constants.EMAIL_MAX_LENGTH:
            raise forms.ValidationError({'email': [_(constants.EMAIL_SIZE)]})
        elif len(email) < constants.EMAIL_MIN_LENGTH:
            raise forms.ValidationError({'email': [_(constants.EMAIL_SIZE)]})

        # Validating password.
        elif len(password) < constants.PASSWORD_MIN_LENGTH:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_SIZE)]})
        elif len(password) > constants.PASSWORD_MAX_LENGTH:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_SIZE)]})
        elif not password.isalnum():
            raise forms.ValidationError({'password': [_(constants.PASSWORD_FORMAT)]})
        elif password != password_confirmation:
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
        elif not phone.isdigit():
            raise forms.ValidationError({'phone': [_(constants.PHONE_NUMBER_FORMAT)]})

        # Validating date of birth.
        elif born < constants.DATE_OF_BIRTH_MIN:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_MIN_ERROR)]})
