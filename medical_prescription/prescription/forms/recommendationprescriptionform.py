# django.
from django import forms


class RecommendationPrescriptionForm(forms.Form):
    """
    Form to associate recommendation to prescription.
    """
    recommendation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Recomendação'}),
                                                         required=False)


    def clean(self, *args, **kwargs):

        return super(RecommendationPrescriptionForm, self).clean(*args, **kwargs)
