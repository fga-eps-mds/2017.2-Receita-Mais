# standard library
import json

# django
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# local django
from user.decorators import is_health_professional
from user.models import (Patient,
                         AssociatedHealthProfessionalAndPatient,
                         )


class AutoCompletePatient(View):
    """
    Responsible for getting patients similar to digits entered to help the user.
    """
    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(AutoCompletePatient, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            search = request.GET.get('term', '')

            queryset_associated_patient = AssociatedHealthProfessionalAndPatient.objects.filter(
                associated_health_professional=request.user,
                is_active=True,
                )

            list_patients = []

            # Encapsulates in a json needed to be sent.
            for model_associated in queryset_associated_patient:
                if search.upper() in model_associated.associated_patient.name.upper():
                    patient_item = {}
                    patient_item['id'] = model_associated.associated_patient.pk
                    patient_item['name'] = model_associated.associated_patient.name
                    patient_item['value'] = model_associated.associated_patient.name
                    patient_item['email'] = model_associated.associated_patient.email

                    list_patients.append(patient_item)

            data = json.dumps(list_patients)
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)
