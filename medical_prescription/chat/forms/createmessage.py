# django
from django import forms

# local django
from chat.models import Message
from django.utils.translation import ugettext_lazy as _
from chat.validators import MessageValidator


class CreateMessage(forms.ModelForm):
    """
    Form to create a custom exam.
    """
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'type': 'text',
                                                            'placeholder': _('Assunto:')}))
    user_to = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'type': 'text',
                                                            'placeholder': _('Para:')}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                         'type': 'text',
                                                         'placeholder': _('Insira aqui sua mensagem')}))

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

        validator = MessageValidator()

        # Fields common all users.
        validator.validator_text(text)
        validator.validator_subject(subject)
        validator.validator_user_to(user_to)
