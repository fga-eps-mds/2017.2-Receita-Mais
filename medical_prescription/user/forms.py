import re
from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from . import constants
from .models import HealthProfessional, Patient, User


class FormattedDateField(forms.DateField):
    widget = forms.DateInput(format='%d/%m/%Y')

    def __init__(self, *args, **kwargs):
        super(FormattedDateField, self).__init__(*args, **kwargs)
        self.input_formats = ('%d/%m/%Y',)


class UserForm(forms.ModelForm):

    date_of_birth = FormattedDateField(initial=date.today)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = User
        fields = [
            'name', 'email', 'date_of_birth', 'phone', 'sex', 'password'
        ]

    def clean(self):
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('confirm_password')
        date_of_birth = self.cleaned_data.get('date_of_birth')

        email_from_database = User.objects.filter(email=email)

        # TODO(Mateus) Refactor date calculation.
        today = date.today()
        born = today.year - date_of_birth.year - \
            ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

        if email_from_database.exists():
            raise ValidationError(constants.EMAIL_EXISTS)
        elif len(password) < constants.PASSWORD_MIN_LENGTH:
            raise forms.ValidationError(constants.PASSWORD_SIZE)
        elif len(password) > constants.PASSWORD_MAX_LENGTH:
            raise forms.ValidationError(constants.PASSWORD_SIZE)
        elif password != password_confirmation:
            raise forms.ValidationError(constants.PASSWORD_MATCH)
        elif len(name) > constants.NAME_MAX_LENGHT:
            raise forms.ValidationError(constants.NAME_SIZE)
        elif len(name) < constants.NAME_MIN_LENGTH:
            raise forms.ValidationError(constants.NAME_SIZE)
        elif len(phone) > constants.PHONE_NUMBER_FIELD_LENGTH:
            raise forms.ValidationError(constants.PHONE_NUMBER_SIZE)
        elif born < constants.DATE_OF_BIRTH_MIN:
            raise forms.ValidationError(constants.DATE_OF_BIRTH_MIN)
        elif email is None:
            raise forms.ValidationError("email inválido")
        else:
            if len(email) > constants.EMAIL_MAX_LENGTH:
                raise forms.ValidationError(constants.EMAIL_SIZE)
            elif len(email) < constants.EMAIL_MIN_LENGTH:
                raise forms.ValidationError(constants.EMAIL_SIZE)


class HealthProfessionalForm(forms.ModelForm):
    class Meta:
        model = HealthProfessional
        fields = ('crm', 'crm_state')

    def clean(self):
        crm = self.cleaned_data.get('crm')
        crm_state = self.cleaned_data.get('crm_state')

        crm_from_database = HealthProfessional.objects.filter(crm=crm)
        crm_state_from_database = HealthProfessional.objects.filter(crm_state=crm_state)

        number_pattern = re.compile(r'^[0-9]*$')

        if len(crm) != constants.CRM_LENGTH:
            raise forms.ValidationError(constants.CRM_SIZE)
        elif len(crm_state) != constants.CRM_STATE_LENGTH:
            raise forms.ValidationError(constants.CRM_STATE_SIZE)
        elif crm_from_database.exists() and crm_state_from_database.exists():
            raise forms.ValidationError(constants.CRM_EXIST)
        elif number_pattern.findall(crm) == []:
            raise forms.ValidationError(constants.CRM_FORMAT)


class PatientForm(UserForm):

    class Meta:
        model = Patient
        fields = [
                'name', 'email', 'date_of_birth', 'phone', 'sex',
                'id_document', 'password'
                ]

    def clean(self):
        id_document = self.cleaned_data.get('id_document')

        if len(id_document) < constants.ID_DOCUMENT_MIN_LENGTH:
            raise forms.ValidationError((constants.ID_DOCUMENT_SIZE))
        elif len(id_document) > constants.ID_DOCUMENT_MAX_LENGTH:
            raise forms.ValidationError((constants.ID_DOCUMENT_SIZE))


class UpdateUserForm(forms.ModelForm):

    date_of_birth = FormattedDateField(initial=date.today)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'name', 'date_of_birth', 'phone', 'sex', 'password'
        ]

    def clean(self):
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('confirm_password')
        date_of_birth = self.cleaned_data.get('date_of_birth')

        today = date.today()
        born = today.year - date_of_birth.year - \
            ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

        if len(password) < constants.PASSWORD_MIN_LENGTH:
            raise forms.ValidationError(constants.PASSWORD_SIZE)
        elif len(password) > constants.PASSWORD_MAX_LENGTH:
            raise forms.ValidationError(constants.PASSWORD_SIZE)
        elif password != password_confirmation:
            raise forms.ValidationError(constants.PASSWORD_MATCH)
        elif len(name) > constants.NAME_MAX_LENGHT:
            raise forms.ValidationError(constants.NAME_SIZE)
        elif len(name) < constants.NAME_MIN_LENGTH:
            raise forms.ValidationError(constants.NAME_SIZE)
        elif len(phone) > constants.PHONE_NUMBER_SIZE:
            raise forms.ValidationError(constants.PHONE_NUMBER_SIZE)
        elif born < constants.DATE_OF_BIRTH_MIN:
            raise forms.ValidationError(constants.DATE_OF_BIRTH_MIN)
