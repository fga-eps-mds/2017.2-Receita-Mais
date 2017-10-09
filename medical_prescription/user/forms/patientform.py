from datetime import date

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from user import constants
from user.models import User, Patient
from user.forms import UserForm, FormattedDateField


class PatientForm(UserForm):
    id_document = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v3__input',
                                                                'placeholder': '* 00000'}))
    date_of_birth = FormattedDateField(initial=date.today)

    class Meta:
        model = Patient
        fields = [
                'name', 'email', 'date_of_birth', 'phone', 'sex',
                'id_document', 'password'
                ]

    def clean(self):
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('confirm_password')
        id_document = self.cleaned_data.get('id_document')
        date_of_birth = self.cleaned_data.get('date_of_birth')

        today = date.today()

        # Validating date of birth Format.
        try:
            born = today.year - date_of_birth.year - \
                ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        except:
            raise forms.ValidationError(constants.DATE_OF_BIRTH_FORMAT)

        email_from_database = User.objects.filter(email=email)

        # Validating email.
        if email_from_database.exists():
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

        # Validating id document.
        elif id_document is not None and len(id_document) < constants.ID_DOCUMENT_MIN_LENGTH:
            raise forms.ValidationError({'id_document': [_(constants.ID_DOCUMENT_SIZE)]})
        elif id_document is not None and len(id_document) > constants.ID_DOCUMENT_MAX_LENGTH:
            raise forms.ValidationError({'id_document': [_(constants.ID_DOCUMENT_SIZE)]})
        elif not id_document.isdigit():
            raise forms.ValidationError({'id_document': [_(constants.ID_DOCUMENT_FORMAT)]})

        # Validating date of birth.
        elif born < constants.DATE_OF_BIRTH_MIN_PATIENT:
            raise forms.ValidationError({'date_of_birth': [_(constants.DATE_OF_BIRTH_MIN_PATIENT_ERROR)]})
