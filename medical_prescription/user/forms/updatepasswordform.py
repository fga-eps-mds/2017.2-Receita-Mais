# django
from django import forms
from user.validators import UserValidator


# This class is responsible for defining the existing fields in the
# password-editing form and for validating such fields.
class UpdatePasswordForm(forms.Form):

    # Form fields to edit password.
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha Atual',
                                                                     'class': 'form-control'}), label='')

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Nova Senha', 'class': 'form-control'}),
                               label='')
    password_confirmation = forms.CharField(widget=forms.PasswordInput(
                            attrs={'placeholder': 'new password confirmation', 'class': 'form-control'}),
                            label='')

    def __init__(self, user, data=None):
        self.user = user
        super(UpdatePasswordForm, self).__init__(data=data)

    # This method makes the vaidations necessary for the completed form to be valid.
    def clean(self, *args, **kwargs):
        old_password = self.cleaned_data.get('old_password')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        # Checking if the old password field matches with the one in database.
        if not self.user.check_password(old_password):
            raise forms.ValidationError('Senha Invalida')

        # Checking if the password confirmation field matches with the password field.
        elif(password != password_confirmation):
            raise forms.ValidationError('As senhas devem ser iguais')

        # Calling the 'Validator' Class to make the new password validation.
        validator = UserValidator()
        validator.validator_password(password, password_confirmation)

        return super(UpdatePasswordForm, self).clean(*args, **kwargs)
