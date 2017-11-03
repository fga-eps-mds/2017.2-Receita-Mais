from django import forms
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
