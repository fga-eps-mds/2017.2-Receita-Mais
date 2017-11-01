# django.
from django import forms


class ExamPrescriptionForm(forms.Form):
    """
    Form to associate exam to prescription.
    """
    exam = forms.CharField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control exam-field',
                                                         'placeholder': 'Nome do Exame'}), required=False)

    exam_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    exam_type = forms.CharField(widget=forms.HiddenInput(), required=False)
