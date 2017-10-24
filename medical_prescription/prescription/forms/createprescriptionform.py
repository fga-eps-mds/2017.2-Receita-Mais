from django import forms


class CreatePrescriptionForm(forms.Form):
    """
    Form to create prescription.
    """
    patient = forms.CharField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control patient-field',
                                                            'placeholder': 'Nome do Paciente:'}), required=False)

    cid = forms.CharField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control',
                                                        'placeholder': 'CID'}), required=False)

    def clean(self):
        """
        Get prescription fields.
        """
        patient = self.cleaned_data.get('patient')
        cid = self.cleaned_data.get('cid')

        # TODO(Ronyell) Validating forms.
