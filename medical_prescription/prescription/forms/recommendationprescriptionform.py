# django.
from django import forms


class RecommendationPrescriptionForm(forms.Form):
    """
    Form to associate recommendation to prescription.
    """
    recommendation = forms.CharField(widget=forms.TextInput(
                                     attrs={
                                            'class': 'transparent-input form-control recommendation-field',
                                            'placeholder': 'Recomendação'}), required=False)

    def clean(self, *args, **kwargs):
        return super(RecommendationPrescriptionForm, self).clean(*args, **kwargs)
