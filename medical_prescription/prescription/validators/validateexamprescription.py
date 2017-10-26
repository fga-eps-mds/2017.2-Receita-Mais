# Django
from django import forms

# Django Local
from exam.models import Exam
from prescription import constants


class ExamPrescriptionValidator():
    """
    Validator of exam in prescriptions.
    """
    def validator_exam(self, exam):
        if exam is not None:
            exam_database = Exam.objects.filter(description=exam)

            if not exam_database.exists() or exam_database is None:
                print("PASSA AQUI")
                raise forms.ValidationError(constants.EXAM_INVALID)
