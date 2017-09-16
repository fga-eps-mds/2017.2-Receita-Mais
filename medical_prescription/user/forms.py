from django import forms


class UserLoginForm(forms.Form):
    '''
    Login Form.
    '''

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
