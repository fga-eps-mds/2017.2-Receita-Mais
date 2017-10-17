from django import forms

from prescription.models import Prescription


class CreatePrescriptionForm(forms.ModelForm):
    class Meta():
        model = Prescription
        fields = ('cid', 'patient',)

    def clean(self):
        """
        Get prescription fields.
        """

        patient = self.cleaned_data.get('patient')
        cid = self.cleaned_data.get('cid')
