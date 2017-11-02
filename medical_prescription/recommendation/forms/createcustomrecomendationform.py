from django import forms


class CreateRecomendationCustomForm(forms.form):
    name = forms.CharField()
    description = forms.CharField()

    def clean(self):
        cleaned_data = super(CreateRecomendationCustomForm, self).clean()
        return cleaned_data
