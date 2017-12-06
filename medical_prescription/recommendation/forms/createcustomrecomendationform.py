from django import forms
from recommendation.validators import CustomRecommendationValidator


class CreateRecomendationCustomForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    validator = CustomRecommendationValidator()

    def get_request(self, request):
        self.request = request

    def clean(self):
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
        self.validator_all(name, description)

    def validator_all(self, name, description):
        self.validator.validator_name(name, self.request)
        self.validator.validator_description(description)
