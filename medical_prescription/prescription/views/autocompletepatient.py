import json

from user.models import Patient

from django.http import HttpResponse
from django.views.generic import View


class AutoCompletePatient(View):
    """
    Responsible for getting patients similar to digits entered to help the user.
    """
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
