# Django
from django import forms
# Models app
from medicine.models import CustomActivePrinciple

# Class create form custom active principle


class CustomActivePrincipleForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'type': 'text'}))

    class Meta:
        model = CustomActivePrinciple
        fields = ['name']
        exclude = ['created_by']
