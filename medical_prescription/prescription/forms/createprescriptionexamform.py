from django import forms

from prescription.models import Prescription


class CreatePrescriptionExamForm(forms.ModelForm):
    patient = forms.CharField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control',
                                                            'placeholder': 'Nome do Paciente:'}))

    cid = forms.CharField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control',
                                                        'placeholder': 'CID'}))

    exam = forms.CharField(widget=forms.TextInput(attrs={'class': 'transparent-input form-control',
                                                         'placeholder': 'Nome do Exame'}))

    class Meta():
        model = Prescription
        fields = ('cid', 'patient',)

    def clean(self):
        """
        Get prescription fields.
        """

        patient = self.cleaned_data.get('patient')
        cid = self.cleaned_data.get('cid')
        exam = self.cleaned_data.get('exam')
