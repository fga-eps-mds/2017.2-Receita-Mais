<<<<<<< HEAD
=======
# standard library
from datetime import date

# Django
from django import forms
# local Django
from .models import Patient, User

from django.core.exceptions import ValidationError
import re
from .import constants

def calculate_age(born):
    """
    This function needs to run unity test.
    """
    today = date.today()
    return today.year - born.year - \
        ((today.month, today.day) < (born.month, born.day))


class FormattedDateField(forms.DateField):
    widget = forms.DateInput(format='%d/%m/%Y')

    def __init__(self, *args, **kwargs):
        super(FormattedDateField, self).__init__(*args, **kwargs)
        self.input_formats = ('%d/%m/%Y',)


class UserForm(forms.ModelForm):

    date_of_birth = FormattedDateField(initial=date.today)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

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

        if email_from_database.exists():
            raise ValidationError("Email ja cadastrado!")
        elif len(password) < 6:
            raise forms.ValidationError("Senha tem que ter mais de 6 caracteres!")
        elif len(password) > 12:
            raise forms.ValidationError("Senha tem que ter menos de 12 caracteres!")
        elif password != password_confirmation:
            raise forms.ValidationError("As senhas não coicidem")
        elif len(email) > 50:
            raise forms.ValidationError("Email deve conter menos de 50 caracteres!")
        elif len(email) < 5:
            raise forms.ValidationError("Email deve conter mais de 5 caracteres!")
        elif len(name) > 50:
            raise forms.ValidationError("Nome deve conter menos de 50 caracteres!")
        elif len(name) < 5:
            raise forms.ValidationError("Nome deve conter mais de 5 caracteres!")
        elif len(phone) > 11:
            raise forms.ValidationError("Telefone deve conter menos de 11 caracteres!")
        elif calculate_age(date_of_birth) < 18:
            raise forms.ValidationError("O usuario ter mais de 18 anos!")
class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['id_document']

    def clean(self):

        id_document = self.cleaned_data.get('id_document')

        if len(id_document) < constants.ID_DOCUMENT_MIN_LENGTH:
            raise forms.ValidationError((constants.ID_DOCUMENT_SIZE))
        elif len(id_document) > constants.ID_DOCUMENT_MAX_LENGTH_MIN_LENGTH:
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

        if len(password) < 6:
            raise forms.ValidationError("Senha tem que ter mais de 6 caracteres!")
        elif len(password) > 12:
            raise forms.ValidationError("Senha tem que ter menos de 12 caracteres!")
        elif password != password_confirmation:
            raise forms.ValidationError("As senhas não coicidem")
        elif len(name) > 50:
            raise forms.ValidationError("Nome deve conter menos de 50 caracteres!")
        elif len(name) < 5:
            raise forms.ValidationError("Nome deve conter mais de 5 caracteres!")
        elif len(phone) > 11:
            raise forms.ValidationError("Telefone deve conter menos de 11 caracteres!")
        elif calculate_age(date_of_birth) < 18:
            raise forms.ValidationError("O usuario ter mais de 18 anos!")
>>>>>>> 42b3c2eb1d8f1ff6864b649d12cab467b262fa3b
