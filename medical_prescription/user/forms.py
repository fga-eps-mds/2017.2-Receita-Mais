from django import forms
from .models import HealthProfessional, User
from django.core.exceptions import ValidationError
# from datetime import date


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'name', 'email', 'password', 'date_of_birth', 'phone', 'sex'
            ]

    def clean(self):
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('confirm_password')

        email_from_database = User.objects.filter(email=email)

        if email_from_database.exists():
            raise ValidationError("Email ja cadastrado!")
        if len(password) < 6:
            raise forms.ValidationError("Senha tem que ter mais de 6 caracteres!")
        if len(password) > 12:
            raise forms.ValidationError("Senha tem que ter menos de 12 caracteres!")
        if password != password_confirmation:
            raise forms.ValidationError("As senhas não coicidem")
        if len(email) > 50:
            raise forms.ValidationError("Email deve conter menos de 50 caracteres!")
        if len(email) < 5:
            raise forms.ValidationError("Email deve conter mais de 5 caracteres!")
        if len(name) > 50:
            raise forms.ValidationError("Nome deve conter menos de 50 caracteres!")
        if len(name) < 5:
            raise forms.ValidationError("Nome deve conter mais de 5 caracteres!")
        if len(phone) > 11:
            raise forms.ValidationError("Telefone deve conter menos de 11 caracteres!")


class HealthProfessionalForm(forms.ModelForm):
    class Meta:
        model = HealthProfessional
        fields = ('crm', 'crm_state')

    def clean(self):
        crm = self.cleaned_data.get('crm')
        crm_state = self.cleaned_data.get('crm_state')

        crm_from_database = User.objects.filter(crm=crm)
        crm_state_from_database = User.objects.filter(crm_state=crm_state)

        if len(crm) != 5:
            raise forms.ValidationError("O CRM deve conter 5 caracteres!")
        elif len(crm_state) != 2:
            raise forms.ValidationError("O estado do crm deve conter 2 caracteres!")
        elif crm_from_database.exists() and crm_state_from_database.exists():
            raise forms.ValidationError("CRM ja existe!")
