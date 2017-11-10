# Django
from django import forms


class CreatePrescriptionForm(forms.Form):
    """
    Form to create prescription.
    """
    patient = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control patient-field',
                                                            'placeholder': 'Nome do Paciente:'}), required=True)
    patient_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    email = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'form-control'}), required=False)

    cid = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'CID'}), required=False)
    cid_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
