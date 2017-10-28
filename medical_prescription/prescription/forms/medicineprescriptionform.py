# django.
from django import forms
from prescription import constants


class MedicinePrescriptionForm(forms.Form):
    """
    Form to associate medicine to prescription.
    """
    medicine = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Medicamento'}))

    medicine_id = forms.IntegerField(widget=forms.HiddenInput())

    medicine_type = forms.CharField(widget=forms.HiddenInput())

    quantity = forms.ChoiceField(choices=constants.QUANTITY_CHOICES,
                                 widget=forms.Select(attrs={'class': 'select-quantity'}))

    posology = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Posologia'}))
