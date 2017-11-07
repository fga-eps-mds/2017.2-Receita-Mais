# django
from django import forms

# local django
from django.utils.translation import ugettext_lazy as _
from chat.validators import MessageValidator


class CreateMessage(forms.Form):
    """
    Form to create a Message.
    """
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'type': 'text',
                                                            'placeholder': _('Assunto:')}))
    user_to = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'type': 'email',
                                                             'id': 'send_email',
                                                             'placeholder': _('Para:')}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'type': 'text',
                                                        'placeholder': _('Insira aqui sua mensagem')}))

    files = forms.FileField(required=False)

    # Get Messages fields.
    def clean(self):

        text = self.cleaned_data.get('text')
        subject = self.cleaned_data.get('subject')
        user_to = self.cleaned_data.get('user_to')
        files = self.cleaned_data['files']

        self.validator_all(text, subject, user_to, files)

        # Verify validations in form.
    # Checks validator in all fields.
    def validator_all(self, text, subject, user_to, files):
        validator = MessageValidator()

        # Fields common all users.
        validator.validator_text(text)
        validator.validator_subject(subject)
        validator.validator_user_to(user_to)

        if files is not None:
            validator.validator_file(files)
        else:
            # Nothing to do.
            pass
