# django.
from django import forms


class MedicinePrescriptionForm(forms.Form):
    """
    Form to associate medicine to prescription.
    """
    medicine = forms.CharField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control exam-field',
                                                             'placeholder': 'Medicamento'}))

    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control exam-field',
                                                                'placeholder': 'Quantidade'}))

    posology = forms.CharField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control exam-field',
                                                                'placeholder': 'Posologia'}))
