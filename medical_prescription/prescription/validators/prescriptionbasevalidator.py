# django
from django import forms
from django.utils.translation import ugettext_lazy as _

# local django
from prescription import constants
from user.constants import (NAME_MAX_LENGHT,
                            NAME_MIN_LENGTH,
                            NAME_SIZE
                            )


class PrescriptionBaseValidator():
    """
    Validator to prescription.
    """

    def validate_patient(self, patient, patient_id):
        if len(patient) > NAME_MAX_LENGHT or len(patient) < NAME_MIN_LENGTH:
            raise forms.ValidationError(_(NAME_SIZE))
        else:
            # Nothing to do.
            pass

    def validate_length_prescription(self, medicine, exam, recommendation):
        valid = False

        if len(medicine) == 1 and len(exam) == 1 and len(recommendation) == 1:

            for medicine_data in medicine:
                if len(medicine_data.data['form_medicine-0-medicine_id']) != 0:
                    valid = True
                else:
                    # Nothing to do.
                    pass
            for exam_data in exam:
                if len(exam_data.data['form_exam-0-exam']) > 5:
                    valid = True
                else:
                    # Nothing to do.
                    pass

            for recommendation_data in recommendation:
                if len(recommendation_data.data['form_recommendation-0-recommendation']) > 5:
                    valid = True
                else:
                    # Nothing to do.
                    pass

        if not valid:
            raise forms.ValidationError(_(constants.EMPTY_PRESCRIPTION))
        else:
            # Nothing to do.
            pass
