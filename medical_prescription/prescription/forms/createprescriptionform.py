# Django
from django import forms
from prescription.validators import PrescriptionBaseValidator


class CreatePrescriptionForm(forms.Form):
    """
    Form to create prescription.
    """
    patient = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control patient-field',
                                                            'placeholder': 'Nome do Paciente:'}), required=True)
    patient_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    email = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'form-control'}), required=False)

    cid = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'CID'}), required=False)
    cid_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    # Get the legth of all form_sets.
    def get_prescription_lengths(self, medicine, exam, recommendation):
        self.medicine = medicine
        self.exam = exam
        self.recommendation = recommendation

    def clean(self, *args, **kwargs):
        patient = self.cleaned_data.get('patient')
        patient_id = self.cleaned_data.get('patient_id')
        email = self.cleaned_data.get('email')
        cid = self.cleaned_data.get('cid')
        cid_id = self.cleaned_data.get('cid_id')

        self.validate_all(patient, patient_id, email, cid, cid_id)

    def validate_all(self, patient, patient_id, email, cid, cid_id):
        validator = PrescriptionBaseValidator()

        validator.validate_patient(patient, patient_id)
        validator.validate_length_prescription(self.medicine, self.exam, self.recommendation)
