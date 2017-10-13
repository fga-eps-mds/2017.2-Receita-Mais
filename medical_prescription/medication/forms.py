from django import forms
from .models import Medication


class CreateMedicationForm(forms.ModelForm):

    # TODO(Felipe) Change for constants in merge.

    name = forms.CharField(max_length=100)
    active_ingredient = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    is_restricted = forms.BooleanField()

    class Meta:
        model = Medication

        fields = ['name', 'active_ingredient', 'description', 'is_restricted']
