from django import forms


class UserLoginForm(forms.Form):
    '''
    Login Form.
    '''

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v3__input',
                                                           'placeholder': '* Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control s-form-v3__input',
                                                                 'placeholder': '* Senha'}))
