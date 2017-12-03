# django
from django import forms

# local django
from exam.models import CustomExam

from exam.validators import CustomExamValidator


class CreateCustomExams(forms.ModelForm):
    """
    Form to create a custom exam.
    """
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        # Define model to form.
        model = CustomExam
        fields = ('description', 'name',)

    def clean(self):
        """
        Get Custom Exam fields.
        """

        description = self.cleaned_data.get('description')
        name = self.cleaned_data.get('name')

        # Verify validations in form.
        self.validator_all(description, name)

    def validator_all(self, description, name):
        """
        Checks validator in all fields.
        """

        validator = CustomExamValidator()

        # Fields common all users.
        validator.validator_name(name)
        validator.validator_description(description)
