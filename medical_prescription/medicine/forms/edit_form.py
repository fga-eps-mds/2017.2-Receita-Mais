from django import forms
from django.utils.translation import ugettext_lazy as _

from medicine.models import ManipulatedMedicine
from medicine import constants


class EditForm(forms.ModelForm):

    recipe_name = forms.CharField(max_length=constants.MAX_LENGTH_NAME,
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'type': 'text',
                                                                'placeholder': _('Nome da Fórmula')}))

    physical_form = forms.CharField(max_length=constants.MAX_LENGTH_PHYSICAL_FORM,
                                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'type': 'text',
                                                                  'placeholder': _('Forma Física')}))

    quantity = forms.FloatField(min_value=constants.MIN_VALUE_QUANTITY,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'type': 'text',
                                                              'placeholder': _('Quantidade')}))

    measurement = forms.CharField(max_length=constants.MAX_LENGTH_PHYSICAL_FORM,
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'type': 'text',
                                                                'placeholder': _('Unidade de Medida')}))

    composition = forms.CharField(widget=forms.Textarea(
                                         attrs={'class': 'form-control',
                                                'cols': '10',
                                                'rows': '5'}))

    class Meta:
        model = ManipulatedMedicine
        fields = ['recipe_name', 'physical_form', 'quantity', 'measurement', 'composition']
