from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from user.models import User
from user import constants


# form to reset password User
class ResetPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control s-form-v4__input g-padding-l-0--xs',
                                                            'placeholder': '* exemplo@exemplo.com'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email_from_database = User.objects.filter(email=email)

        if email_from_database.exists():
            pass
        else:
            raise ValidationError({'email': [_(constants.EMAIL_EXISTS)]})
        return super(ResetPasswordForm, self).clean(*args, **kwargs)
