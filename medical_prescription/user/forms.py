from django import forms
from .models import HealthProfessional, User
from django.core.exceptions import ValidationError

from datetime import date
import re


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

        if len(crm) != 5:
            raise forms.ValidationError("O CRM deve conter 5 caracteres!")
        elif len(crm_state) != 2:
            raise forms.ValidationError("O estado do crm deve conter 2 caracteres!")
        elif crm_from_database.exists() and crm_state_from_database.exists():
            raise forms.ValidationError("CRM ja existe!")
        elif number_pattern.findall(crm) == []:
            raise forms.ValidationError("A CRM só pode conter números!")


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
