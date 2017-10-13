# django
from django import forms
from django.utils.translation import ugettext_lazy as _

# local django
from exam import constants
from exam.models import CustomExam


class CustomExamValidator():
    """
    Validating Custom Exam fields.
    """

    def validator_description(self, description):
        """
        Validating description.
        """

        if description is not None and len(description) > constants.DESC_MAX_LENGTH:
            raise forms.ValidationError({'description': [_(constants.DESC_SIZE)]})
        elif description is not None and len(description) < constants.DESC_MIN_LENGTH:
            raise forms.ValidationError({'description': [_(constants.DESC_SIZE)]})

    def validator_name(self, name):
        """
        Validating name.
        """
        name_base = CustomExam.objects.filter(name=name)

        if name is not None and len(name) > constants.NAME_MAX_LENGTH:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif name is not None and len(name) < constants.NAME_MIN_LENGTH:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif name_base.exists():
            raise forms.ValidationError({'name': [_(constants.NAME_EXISTS)]})

    def validator_name_update(self, name):
        """
        Validating name.
        """

        if name is not None and len(name) > constants.NAME_MAX_LENGTH:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
        elif name is not None and len(name) < constants.NAME_MIN_LENGTH:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE)]})
