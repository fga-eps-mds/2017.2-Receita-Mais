from django import forms

from .models import User

class UserLoginForm(forms.Form):
    '''
        Login Form.
    '''

    email=forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=[
            'email',
            'password'
        ]
