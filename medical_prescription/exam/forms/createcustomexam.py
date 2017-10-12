# django
from django import forms

# local django
from exam.models import CustomExam

from exam.validators import CustomExamValidator


class CreateCustomExams(forms.Form):
    """
    Form to create a custom exam.
    """

    class Meta:
        # Define model to form.
        model = CustomExam
        fields = ('description',)

    def clean(self):
        """
        Get Custom Exam fields.
        """

        description = self.cleaned_data.get('description')

        # Verify validations in form.
        self.validator_all(description)

    def validator_all(self, description):
        """
        Checks validator in all fields.
        """

        validator = CustomExamValidator()

        # Fields common all users.
        validator.validator_description(description)
