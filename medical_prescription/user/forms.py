from django import forms
from .models import HealthProfessional


class UserLoginForm(forms.Form):
    '''
    Login Form.
    '''

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class HealthProfessionalForm(forms.ModelForm):

    class Meta:
        model = HealthProfessional
        fields = ('crm', 'crm_state')
        # ('first_name', 'last_name', 'date_of_birth', 'phone', 'email', 'sex')


# fom to reset password User
class ResetPasswordForm(forms.Form):
    email = forms.EmailField(label='email', max_length=250)
