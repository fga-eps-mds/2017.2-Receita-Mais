from django import forms
from recommendation.validators import CustomRecommendationValidator


class CreateRecomendationCustomForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    validator = CustomRecommendationValidator()

    def clean(self):
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
        self.validator_all(name, description)

    def validator_all(self, name, description):
        self.validator.validator_name(name)
        self.validator.validator_description(description)
