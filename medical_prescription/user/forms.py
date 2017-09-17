from django import forms
from .models import HealthProfessional


class HealthProfessionalForm(forms.ModelForm):

    class Meta:
        model = HealthProfessional
        fields = ('crm', 'crm_state')
        # ('first_name', 'last_name', 'date_of_birth', 'phone', 'email', 'sex')