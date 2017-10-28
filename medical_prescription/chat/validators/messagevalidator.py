# django
from django import forms
from django.utils.translation import ugettext_lazy as _

# local django
from chat import constants
from user.models import User


class MessageValidator():
    """
    Validating custom Message and Response fields.
    """

    # Validating text.
    def validator_text(self, text):
        if text is not None and len(text) > constants.MAX_LENGTH_TEXT_MESSAGE:
            raise forms.ValidationError({'text': [_(constants.TEXT_SIZE)]})

    # Validanting user.
    def validator_user_to(self, user_to):

        email_from_database = User.objects.filter(email=user_to)

        if not email_from_database.exists():
            raise forms.ValidationError({'user_to': [_(constants.USER_EXISTS)]})

    # Validanting subject.
    def validator_subject(self, subject):

        if subject is not None and len(subject) > constants.MAX_LENGTH_TEXT_SUBJECT:
            raise forms.ValidationError({'subject': [_(constants.SUBJECT_SIZE)]})
