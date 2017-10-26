# django.
from django import forms
from prescription import constants


class MedicinePrescriptionForm(forms.Form):
    """
    Form to associate medicine to prescription.
    """
    medicine = forms.CharField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control exam-field',
                                                             'placeholder': 'Medicamento'}))

    medicine_id = forms.IntegerField(widget=forms.HiddenInput())

    quantity = forms.ChoiceField(choices=constants.QUANTITY_CHOICES)

    posology = forms.CharField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control exam-field',
                                                             'placeholder': 'Posologia'}))
