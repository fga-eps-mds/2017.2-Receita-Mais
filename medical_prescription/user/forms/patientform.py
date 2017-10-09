# standard library
from datetime import date

# Django
from django import forms

# Local Django
from user.models import Patient
from user.forms import UserForm, FormattedDateField
from user.validators import PatientValidator


class PatientForm(UserForm):
    id_document = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-form-v3__input',
                                                                'placeholder': '* 00000'}))
    date_of_birth = FormattedDateField(initial=date.today)

    class Meta:
        model = Patient
        fields = [
                'name', 'email', 'date_of_birth', 'phone', 'sex',
                'id_document', 'password'
                ]

    def clean(self):
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('confirm_password')
        id_document = self.cleaned_data.get('id_document')
        date_of_birth = self.cleaned_data.get('date_of_birth')
        self.validator_all(name, phone, email, password, password_confirmation, id_document, date_of_birth)

    def validator_all(self, name, phone, email, password, password_confirmation, id_document, date_of_birth):
        validator = PatientValidator()
        validator.validator_email(email)
        validator.validator_password(password, password_confirmation)
        validator.validator_name(name)
        validator.validator_phone_number(phone)
        validator.validator_document(id_document)
        validator.validator_date_of_birth(date_of_birth)
