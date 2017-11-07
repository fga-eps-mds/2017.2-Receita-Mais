# django
from django import forms

# local django
from django.utils.translation import ugettext_lazy as _
from chat.validators import MessageValidator


class CreateResponse(forms.Form):
    """
    Form to create a Reponse.
    """
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'type': 'text',
                                                        'placeholder': _('Insira aqui sua mensagem')}))

    files = forms.FileField(required=False)

    # Get Messages fields.
    def clean(self):

        text = self.cleaned_data.get('text')
        files = self.cleaned_data['files']

        # Verify validations in form.
        self.validator_all(text, files)

    # Checks validator in all fields.
    def validator_all(self, text, files):

        validator = MessageValidator()

        validator.validator_text(text)

        if files is not None:
            validator.validator_file(files)
        else:
            # Nothing to do.
            pass
