# django
from django import forms
from django.utils.translation import ugettext_lazy as _

# local django
from chat import constants
from user.models import (User,
                         Patient,
                         HealthProfessional,
                         AssociatedHealthProfessionalAndPatient)


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

    def validator_user_to_is_health_professional(self, user_to):

        email_health_professional = HealthProfessional.objects.filter(email=user_to)

        if email_health_professional.exists():
            raise forms.ValidationError({'user_to': [_(constants.USER_TO_IS_HEALTH_PROFESSIONAL)]})

    def validator_user_to_not_linked(self, user_to, user_from):

        patient = Patient.objects.get(email=user_to)

        relation = AssociatedHealthProfessionalAndPatient.objects.filter(associated_health_professional=user_from,
                                                                         associated_patient=patient,
                                                                         is_active=True)

        if relation.exists() is False:
            raise forms.ValidationError({'user_to': [_(constants.USER_TO_IS_NOT_LINKED)]})

    # Validanting subject.
    def validator_subject(self, subject):

        if subject is not None and len(subject) > constants.MAX_LENGTH_TEXT_SUBJECT:
            raise forms.ValidationError({'subject': [_(constants.SUBJECT_SIZE)]})

    def validator_file(self, content):
        content_type = content.content_type.split('/')[1]
        if content_type in constants.CONTENT_TYPES:
            if content._size > constants.MAX_UPLOAD_SIZE:
                raise forms.ValidationError({'files': [_(constants.FILE_SIZE)]})
        else:
            raise forms.ValidationError({'files': [_(constants.FORMAT_ERROR)]})
