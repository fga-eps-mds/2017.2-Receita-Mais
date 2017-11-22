# Django
from django import forms

# Local Django
from django.utils.translation import ugettext_lazy as _
from prescription import constants


class PatternForm(forms.Form):
    name = forms.CharField(max_length=constants.MAX_LENGTH_NAME,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'type': 'text',
                                                         'placeholder': _('Nome de Modelo')}))

    clinic = forms.CharField(max_length=constants.MAX_LENGTH_CLINIC,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'type': 'text',
                                                           'placeholder': _('Clinica')}))

    header = forms.CharField(max_length=constants.MAX_LENGTH_HEADER,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'type': 'text',
                                                           'placeholder': _('Header')}))

    footer = forms.CharField(max_length=constants.MAX_LENGTH_FOOTER,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'type': 'text',
                                                           'placeholder': _('Footer')}))

    pagesize = forms.ChoiceField(choices=constants.PAGE_SIZE_CHOICE)

    logo = forms.FileField(required=False)

    font = forms.ChoiceField(choices=constants.FONT_CHOICE)
    font_size = forms.ChoiceField(choices=constants.FONT_SIZE_CHOICE)
