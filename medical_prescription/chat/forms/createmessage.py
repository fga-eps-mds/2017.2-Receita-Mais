# django
from django import forms

# local django
from chat.models import Message

from exam.validators import CustomExamValidator


class CreateMessage(forms.ModelForm):
    """
    Form to create a custom exam.
    """
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        # Define model to form.
        model = Message
        fields = ('text', 'subject', 'user_to')

    def clean(self):
        """
        Get Custom Exam fields.
        """

        text = self.cleaned_data.get('text')
        subject = self.cleaned_data.get('subject')
        user_to = self.cleaned_data.get('subject')

        # Verify validations in form.
        self.validator_all(text, subject, user_to)

    def validator_all(self, text, subject, user_to):
        """
        Checks validator in all fields.
        """

        validator = CustomExamValidator()

        # Fields common all users.
        validator.validator_name(text)
        validator.validator_subject(subject)
        validator.validator_user_to(user_to)
