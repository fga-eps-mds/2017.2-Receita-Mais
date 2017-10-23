# django
from django import forms
from django.utils.translation import ugettext_lazy as _

# local django
from chat import constants
from chat.models import Message


class MessageValidator():
    """
    Validating Custom Exam fields.
    """

    def validator_text(self, text):
        """
        Validating text.
        """

        if text is not None and len(text) > constants.MAX_LENGTH_TEXT_SUBJECT:
            raise forms.ValidationError({'text': [_(constants.TEXT_SIZE)]})

    def validator_user_to(self, name):
        """
        Validating user.
        """
        user_base = Message.objects.filter(name=name)

        if name is not None and len(name) > constants.NAME_MAX_LENGTH:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif name is not None and len(name) < constants.NAME_MIN_LENGTH:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif not user_base.exists():
            raise forms.ValidationError({'name': [_(constants.USER_EXISTS)]})

    def validator_subject(self, subject):
        """
        Validating subject.
        """

        if subject is not None and len(subject) > constants.MAX_LENGTH_TEXT_SUBJECT:
            raise forms.ValidationError({'subject': [_(constants.SUBJECT_SIZE)]})
