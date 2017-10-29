# django.
from django import forms

# Django Local
from prescription.validators import ExamPrescriptionValidator


class ExamPrescriptionForm(forms.Form):
    """
    Form to associate exam to prescription.
    """
    exam = forms.CharField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control exam-field',
                                                         'placeholder': 'Nome do Exame'}))

    exam_id = forms.IntegerField(widget=forms.HiddenInput())
    exam_type = forms.CharField(widget=forms.HiddenInput())

    validator = ExamPrescriptionValidator()

    def clean(self):
        exam = self.cleaned_data.get('exam')

        self.validator_all(exam)

    def validator_all(self, exam):
        self.validator.validator_exam(exam)
