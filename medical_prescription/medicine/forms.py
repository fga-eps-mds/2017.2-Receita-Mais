from django import forms
from .models import CustomActivePrinciple


class CustomActivePrincipleForm(forms.ModelForm):

    class Meta:
        model = CustomActivePrinciple
        fields = ['name']
        exclude = ['created_by']
