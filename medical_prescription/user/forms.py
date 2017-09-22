from django import forms
from .models import HealthProfessional
from .models import User


class UserLoginForm(forms.Form):
    '''
    Login Form.
    '''

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, label=('password'))


class HealthProfessionalForm(forms.ModelForm):

    class Meta:
        model = HealthProfessional
        fields = ('crm', 'crm_state')
        # ('first_name', 'last_name', 'date_of_birth', 'phone', 'email', 'sex')


# fom to reset password User
class ResetPasswordForm(forms.Form):
    email = forms.EmailField(label='email', max_length=250)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email_from_database = User.objects.filter(email=email)

        if email_from_database.exists():
            pass
        else:
            raise forms.ValidationError('this email is not registered')
        return super(ResetPasswordForm, self).clean(*args, **kwargs)


class ConfirmPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}), label='')
    password_confirmation = forms.CharField(widget=forms.PasswordInput(
                            attrs={'placehold': 'password confirmation'}),
                            label='')
