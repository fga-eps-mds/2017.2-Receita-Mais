# Django
from django import forms

from prescription.validators import EmailValidator


class CreatePrescriptionForm(forms.Form):
    """
    Form to create prescription.
    """
    patient = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control patient-field',
                                                            'placeholder': 'Nome do Paciente:'}), required=True)
    patient_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'exemplo@exemplo.com'}), required=False)

    cid = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'CID'}), required=False)
    cid_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    # Validating patient email.
    def clean(self):
        validator = EmailValidator()

        email = self.cleaned_data.get('email')

        validator.validator_email(email)
