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
    image = forms.FileField(required=False)

    # Get Messages fields.
    def clean(self):

        text = self.cleaned_data.get('text')

        # Verify validations in form.
        self.validator_all(text)

    # Checks validator in all fields.
    def validator_all(self, text):

        validator = MessageValidator()

        # Fields common all users.
        validator.validator_text(text)
