# django
from django import forms
from django.utils.translation import ugettext_lazy as _

# local django
from exam.models import CustomExam
from exam import constants


class CustomExamValidator():
    """
    Validating Custom Exam fields.
    """

    def validator_description(self, description):
        """
        Validating description.
        """

        description = CustomExam.objects.filter(description=description)

        if description is not None and len(description) > constants.DESC_MAX_LENGTH:
            raise forms.ValidationError({'description': [_(constants.DESC_SIZE)]})
        elif description is not None and len(description) < constants.DESC_MIN_LENGTH:
            raise forms.ValidationError({'description': [_(constants.DESC_SIZE)]})
