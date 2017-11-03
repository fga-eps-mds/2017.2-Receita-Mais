# Django
from django import forms
from django.utils.translation import ugettext_lazy as _

# Django local
from recommendation import constants


class CustomRecommendationValidator(object):
    """
    docstring for CustomRecommendationValidator.
    """
    def validator_name(self, name):
        if name is not None and len(name) < constants.MIN_NAME:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE_MIN)]})
        elif name is not None and len(name) > constants.MAX_NAME:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE_MAX)]})
        else:
            # Nothing to do.
            pass

    def validator_description(self, description):
        if description is not None and len(description) < constants.MAX_DESCRIPTION:
            raise forms.ValidationError({'name': [_(constants.DESCRIPTION_SIZE_MAX)]})
        elif description is not None and len(description) > constants.MIN_DESCRIOPTION:
            raise forms.ValidationError({'name': [_(constants.DESCRIPTION_SIZE_MIN)]})
