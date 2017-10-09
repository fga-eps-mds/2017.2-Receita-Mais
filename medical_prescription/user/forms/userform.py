# django
from django import forms

# local django
from user.forms import FormattedDateField
from user import constants
from user.models import User


class UserForm(forms.ModelForm):
    """
    Define fields in user form.
    """
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v3__input',
                                                         'placeholder': '* João da Silva '}))
    date_of_birth = FormattedDateField(widget=forms.DateInput(attrs={'class': 'form-control s-form-v3__input',
                                                                     'placeholder': '*Ex: dd/mm/aaaa'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control s-form-v3__input',
                                                                 'placeholder': '*********'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control s-form-v3__input',
                                                                         'placeholder': '*********'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control s-form-v3__input',
                                                            'placeholder': '* exemplo@exemplo.com'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v3__input',
                                                          'placeholder': '* (xx)xxxxx-xxxx'}))
    sex = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control s-form-v3__input'}),
                            choices=constants.SEX_CHOICE)

    class Meta:
        # Define model to User.
        model = User
        fields = [
            'name', 'email', 'date_of_birth', 'phone', 'sex', 'password'
        ]
