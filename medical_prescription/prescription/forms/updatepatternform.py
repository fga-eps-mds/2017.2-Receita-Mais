# Django
from django import forms
from django.db import models

# Local Django
from django.utils.translation import ugettext_lazy as _
from prescription import constants
from prescription.models import Pattern
from prescription.validators import PatternValidator


class UpdatePatternForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'type': 'text',
                                                         'placeholder': _('Nome de Modelo')}))

    clinic = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'type': 'text',
                                                           'placeholder': _('Clinica')}))

    header = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'type': 'text',
                                                           'placeholder': _('Header')}))

    footer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'type': 'text',
                                                           'placeholder': _('Footer')}))

    pagesize = forms.ChoiceField(choices=constants.PAGE_SIZE_CHOICE)

    logo = forms.FileField(required=False, widget=forms.FileInput, initial='')

    font = forms.ChoiceField(choices=constants.FONT_CHOICE)
    font_size = forms.ChoiceField(choices=constants.FONT_SIZE_CHOICE)

    class Meta:
        model = Pattern
        fields = ['name', 'clinic', 'header', 'footer', 'pagesize', 'logo', 'font', 'font_size']

    # Get Pattern fields.
    def clean(self):

        name = self.cleaned_data.get('name')
        clinic = self.cleaned_data.get('clinic')
        header = self.cleaned_data.get('header')
        footer = self.cleaned_data.get('footer')
        files = self.cleaned_data['logo']
        self.validator_all(name, clinic, header, footer, files)

    # Verify validations in form.
    def validator_all(self, name, clinic, header, footer, files):
        validator = PatternValidator()

        # Fields common all users.
        validator.validator_name(name)
        validator.validator_clinic(clinic)
        validator.validator_header(header)
        validator.validator_footer(footer)

        if files is None or type(files) == models.fields.files.FieldFile:
            pass
        else:
            validator.validator_file(files)
