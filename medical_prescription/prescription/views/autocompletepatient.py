# standard library
import json

# django
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# local django
from user.decorators import is_health_professional
from user.models import Patient


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

            # TODO(Ronyell) Switch to the health care professional's patients.
            queryset = Patient.objects.filter(name__icontains=search)[:5]
            list_patients = []

            # Encapsulates in a json needed to be sent.
            for patient in queryset:
                patient_item = {}
                patient_item['id'] = patient.id
                patient_item['name'] = patient.name
                patient_item['value'] = patient.name

                list_patients.append(patient_item)

            data = json.dumps(list_patients)
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)
