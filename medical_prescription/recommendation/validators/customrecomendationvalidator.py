# Django
from django import forms
from django.utils.translation import ugettext_lazy as _

# Django local
from recommendation import constants
from recommendation.models import CustomRecommendation


class CustomRecommendationValidator(object):
    """
     Validation class to validate CustomRecommendationValidator.
    """
    def validator_name(self, name, request):

        data_base_custom_recommendation = CustomRecommendation.objects.filter(
            name=name,
            health_professional=request.user
            )

        if name is not None and len(name) < constants.MIN_NAME:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE_MIN)]})
        elif name is not None and len(name) > constants.MAX_NAME:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE_MAX)]})
        elif data_base_custom_recommendation.exists():
            raise forms.ValidationError({'name': [_(constants.NAME_DUPLICATED)]})
        else:
            # Nothing to do.
            pass

    # Validate the field recommendation custom recommendation.
    def validator_description(self, description):
        if description is not None and len(description) > constants.MAX_DESCRIPTION:
            raise forms.ValidationError({'name': [_(constants.DESCRIPTION_SIZE_MAX)]})
        elif description is not None and len(description) < constants.MIN_DESCRIPTION:
            raise forms.ValidationError({'name': [_(constants.DESCRIPTION_SIZE_MIN)]})

    # Validate name in update custom recommendation form.
    def validator_name_update(self, name):
        if name is not None and len(name) < constants.MIN_NAME:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE_MIN)]})
        elif name is not None and len(name) > constants.MAX_NAME:
            raise forms.ValidationError({'name': [_(constants.NAME_SIZE_MAX)]})
        else:
            # Nothing to do.
            pass
