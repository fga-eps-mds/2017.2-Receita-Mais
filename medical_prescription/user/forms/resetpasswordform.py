# django
from django import forms

# local django
from user.validators import UserValidator


class ResetPasswordForm(forms.Form):
    """
    Form to reset password User
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control s-form-v4__input g-padding-l-0--xs',
                                                            'placeholder': '* exemplo@exemplo.com'}))

    def clean(self, *args, **kwargs):
        """
        Get patient fields.
        """

        email = self.cleaned_data.get('email')

        # Verify validations in form.
        self.validator_all(email)

        return super(ResetPasswordForm, self).clean(*args, **kwargs)

    def validator_all(self, email):
        """
        Checks validator in all fields.
        """

        validator = UserValidator()
        validator.validator_email_in_reset_password(email)
