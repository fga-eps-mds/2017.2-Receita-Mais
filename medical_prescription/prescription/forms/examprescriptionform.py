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

    validator = ExamPrescriptionValidator()

    def clean(self):
        exam = self.cleaned_data['exam']

        self.validator_all(exam)

    def validator_all(self, exam):
        self.validator.validator_exam(exam)
