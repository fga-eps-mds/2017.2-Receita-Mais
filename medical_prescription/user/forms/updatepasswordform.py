# django
from django import forms
from user.validators import UserValidator


class UpdatePasswordForm(forms.Form):
    """
    Form to confirm password.
    """
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'old password'}),
                                   label='')
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'new password'}),
                                   label='')
    new_password_confirmation = forms.CharField(widget=forms.PasswordInput(
                            attrs={'placeholder': 'new password confirmation'}),
                            label='')

    def __init__(self, user, data=None):
        self.user = user
        super(UpdatePasswordForm, self).__init__(data=data)

    def clean(self, *args, **kwargs):
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        new_password_confirmation = self.cleaned_data.get('new_password_confirmation')

        if not self.user.check_password(old_password):
            raise forms.ValidationError('Senha Invalida')
        elif(new_password != new_password_confirmation):
            raise forms.ValidationError('As senhas devem ser iguais')

        validator = UserValidator()
        validator.validator_password(new_password, new_password_confirmation)

        return super(UpdatePasswordForm, self).clean(*args, **kwargs)

    def verify_password(self, password):
        """
        Verifies if the given password matches the one in the database.
        """

        return self.instance.check_password(password)
