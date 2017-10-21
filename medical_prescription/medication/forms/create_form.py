from django import forms
from django.utils.translation import ugettext_lazy as _

from medication.models import Medication


class CreateMedicationForm(forms.ModelForm):

    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'type': 'text',
                                                         'placeholder': _('Nome')}))

    laboratory = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'type': 'text',
                                                               'placeholder': _('Laboratório')}))

    active_ingredient = forms.CharField(max_length=100,
                                        widget=forms.TextInput(attrs={'class': 'form-control',
                                                                      'type': 'text',
                                                                      'placeholder': _('Princípio Ativo')}))
    description = forms.CharField(widget=forms.Textarea(
                                  attrs={'class': 'form-control',
                                         'cols': '10',
                                         'rows': '5'}))
    is_restricted = forms.BooleanField(required=False)

    class Meta:
        model = Medication
        fields = ['name', 'active_ingredient', 'laboratory', 'description']
