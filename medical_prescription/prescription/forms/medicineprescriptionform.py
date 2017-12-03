# django.
from django import forms

# Django Local
from prescription import constants


class MedicinePrescriptionForm(forms.Form):
    """
    Form to associate medicine to prescription.
    """
    medicine = forms.CharField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control medicine-field',
                                                             'placeholder': 'Medicamento'}), required=False)

    medicine_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    medicine_type = forms.CharField(widget=forms.HiddenInput(), required=False)

    quantity = forms.ChoiceField(choices=constants.QUANTITY_CHOICES,
                                 widget=forms.Select(attrs={'class': 'form-control'}), required=False)

    posology = forms.CharField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control medicine-field',
                                                             'placeholder': 'Posologia'}), required=False)

    via = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control',
                                                       'placeholder': 'Via'}),
                            choices=constants.VIA_CHOICES)
