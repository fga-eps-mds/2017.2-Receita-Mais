# Django
from django import forms
# Models app
from medicine.models import CustomActivePrinciple

# Class create form custom active principle


class CustomActivePrincipleForm(forms.ModelForm):

    class Meta:
        model = CustomActivePrinciple
        fields = ['name']
        exclude = ['created_by']
