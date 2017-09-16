"""Forms"""

# Django.
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

# Local Django.
from .models import User
from .import constants
from user.models import Patient


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('name', 'date_of_birth', 'phone', 'email', 'sex',
                  'id_document')


class PatientRegisterForm(forms.ModelForm):
    # Form Fields.
    name = forms.CharField(label=constants.NAME,
                            max_length=constants.NAME_MAX_LENGHT,
                            min_length=constants.NAME_MIN_LENGTH)

    password = forms.CharField(widget=forms.PasswordInput,
                               label=_('Password'))

    password_confirmation = forms.CharField(widget=forms.PasswordInput,
                                            label=_('Password Confirmation'))

    date_of_birth = forms.DateField(label=constants.DATE_OF_BIRTH)

    phone = forms.CharField(label = constants.PHONE_NUMBER,
                            max_length=constants.PHONE_NUMBER_MAX_LENGTH,
                            min_length=constants.PHONE_NUMBER_MIN_LENGTH)

    sex = forms.CharField(label = constants.SEX)

    id_document = forms.IntegerField(label=constants.ID_DOCUMENT,
                               max_length=constants.ID_DOCUMENT_MAX_LENGTH_MAX_LENGHT,
                               min_length=constants.ID_DOCUMENT_MIN_LENGTH)
    class Meta:
        model = User
        fields = ['name', 'date_of_birth', 'phone', 'email', 'sex',
                  'id_document']

    # Front-end validation function for register page.
    def clean(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        date_of_birth = self.cleaned_data.get('date_of_birth')
        phone = self.cleaned_data.get('phone')
        sex = self.cleaned_data.get('sex')
        id_document = self.cleaned_data.get('id_document')

        if len(password) < constants.PASSWORD_MIN_LENGTH:
            raise forms.ValidationError(_(constants.PASSWORD_SIZE))
        elif len(password) > constants.PASSWORD_MAX_LENGTH:
            raise forms.ValidationError(_(constants.PASSWORD_SIZE))
        elif password != password_confirmation:
            raise forms.ValidationError(_(constants.PASSWORD_NOT_EQUAL))
        elif len(name) > constants.NAME_MAX_LENGHT:
            raise forms.ValidationError(_(constants.NAME_SIZE))
        elif len(name) < constants.NAME_MIN_LENGHT:
            raise forms.ValidationError(_(constants.NAME_SIZE))
        elif len(phone) > constants.PHONE_NUMBER_MAX_LENGTH:
            raise forms.ValidationError(_(constants.PHONE_NUMBER_SIZE))
        elif len(phone) < constants.PHONE_NUMBER_MIN_LENGTH:
            raise forms.ValidationError(_(constants.PHONE_NUMBER_SIZE))
        elif len(id_document) < constants.ID_DOCUMENT_MIN_LENGTH:
            raise forms.ValidationError(_(constants.ID_DOCUMENT_SIZE))
        elif len(id_document) < constants.ID_DOCUMENT_MAX_LENGTH_MIN_LENGTH:
            raise forms.ValidationError(_(constants.ID_DOCUMENT_SIZE))

        return super(PatientRegisterForm, self).clean(*args, **kwargs)
