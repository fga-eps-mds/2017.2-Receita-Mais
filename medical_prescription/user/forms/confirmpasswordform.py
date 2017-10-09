from django import forms


class ConfirmPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}),
                               label='')
    password_confirmation = forms.CharField(widget=forms.PasswordInput(
                            attrs={'placehold': 'password confirmation'}),
                            label='')

    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if(password != password_confirmation):
            raise forms.ValidationError('As senhas devem ser iguais')
        else:
            # Nothing to do.
            pass

        return super(ConfirmPasswordForm, self).clean(*args, **kwargs)
