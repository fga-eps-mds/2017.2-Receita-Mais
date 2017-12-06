# django
from django import forms

# local django
from recommendation.models import CustomRecommendation
from recommendation.validators import CustomRecommendationValidator
from exam import constants


class UpdateCustomRecommendationForm(forms.ModelForm):
        """
        Form to edit a custom recommendation.
        """
        name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        recommendation = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

        class Meta:
            # Define model to form.
            model = CustomRecommendation
            fields = ('recommendation', 'name',)

        def get_pk(self, pk):
            self.pk = pk

        def clean(self):
            """
            Get Custom Recommendation fields.
            """
            recommendation = self.cleaned_data.get('recommendation')
            name = self.cleaned_data.get('name')

            exists = CustomRecommendation.objects.get(pk=self.pk)

            name_base = CustomRecommendation.objects.filter(name=name)

            if name_base.exists() and exists.name != name:
                raise forms.ValidationError({'name': [(constants.NAME_EXISTS)]})

            # Verify validations in form.
            self.validator_all(recommendation, name)

        def validator_all(self, description, name):
            """
            Checks validator in all fields.
            """

            validator = CustomRecommendationValidator()

            validator.validator_name_update(name)
            validator.validator_description(description)
