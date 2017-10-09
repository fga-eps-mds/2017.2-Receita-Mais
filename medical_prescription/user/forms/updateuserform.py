from datetime import date

from django import forms

from user.forms import FormattedDateField
from user.models import User
from user.validators import UserValidator


class UpdateUserForm(forms.ModelForm):

    # It verifies if the given password matches the one in the database.
    def verify_password(self, password):
        return self.instance.check_password(password)

    date_of_birth = FormattedDateField(initial=date.today)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'name', 'date_of_birth', 'phone', 'sex'
        ]

    def clean(self):
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        date_of_birth = self.cleaned_data.get('date_of_birth')
        self.validator_all(name, phone, password, date_of_birth)

    def validator_all(self, name, phone, password, date_of_birth):
        validator = UserValidator()
        validator.validator_password(password, password)
        validator.validator_name(name)
        validator.validator_phone_number(phone)
        validator.validator_date_of_birth(date_of_birth)
