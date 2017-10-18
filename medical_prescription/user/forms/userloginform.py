# django
from django import forms
from django.utils.translation import ugettext_lazy as _


class UserLoginForm(forms.Form):
    '''
    Login Form.
    '''
    password_placeholder = _('Senha')

    email = forms.EmailField(widget=forms.TextInput(
                              attrs={'class': 'form-control s-form-v3__input',
                                     'placeholder': 'Email'}))

    password = forms.CharField(widget=forms.PasswordInput(
                               attrs={'class': 'form-control s-form-v3__input',
                                      'placeholder': password_placeholder}))
