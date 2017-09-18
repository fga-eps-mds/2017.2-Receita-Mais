from django import forms
from .models import HealthProfessional, User
# from datetime import date


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'name', 'email', 'password', 'date_of_birth', 'phone', 'sex')

    def clean(self):
        pass


class HealthProfessionalForm(forms.ModelForm):
    class Meta:
        model = HealthProfessional
        fields = ('crm', 'crm_state')

    def clean(self):
        pass
