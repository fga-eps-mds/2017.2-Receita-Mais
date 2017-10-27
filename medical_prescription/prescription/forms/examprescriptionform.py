# django.
from django import forms


class ExamPrescriptionForm(forms.Form):
    """
    Form to associate exam to prescription.
    """
    exam = forms.CharField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control exam-field',
                                                         'placeholder': 'Nome do Exame'}))
