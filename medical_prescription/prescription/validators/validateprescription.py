# Django
from django import forms

# Django Local
from disease.models import Disease
from prescription import constants


class PrescriptionValidator():
    """
    Validation of Prescription.
    """
    def validator_cid(self, cid):
        if cid is not None:
            disease_cid_database = Disease.objects.filter(id_cid_10=cid)

            if not disease_cid_database.exists:
                raise forms.ValidationError(constants.CID_INVALID)
