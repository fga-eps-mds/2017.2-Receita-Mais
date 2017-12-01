import json

from django.views.generic import View
from django.http import HttpResponse

from user.models import (AssociatedHealthProfessionalAndPatient,
                         Patient)


class AutoCompleteEmail(View):
    """
    Return a query of email users.
    """
    def get(self, request, *args, **kwargs):

        if request.is_ajax():

            search = request.GET.get('term', '')
            query_email = Patient.objects.filter(email__icontains=search)[:5]
            query_name = Patient.objects.filter(name__icontains=search)[:5]
            query_list = []

            for patient in query_email:
                relation = AssociatedHealthProfessionalAndPatient.objects.get(associated_health_professional=request.user,
                                                                              associated_patient=patient,
                                                                              is_active=True)
                self.create_item(query_list, patient)

            for patient in query_name:
                relation = AssociatedHealthProfessionalAndPatient.objects.get(associated_health_professional=request.user,
                                                                              associated_patient=patient,
                                                                              is_active=True)

                if self.check_query_list(query_list, relation.associated_patient) is False:
                    self.create_item(query_list, patient)

            data = json.dumps(query_list)
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)

    def create_item(self, query_list, patient):
        patient_item = {}
        patient_item['value'] = patient.email
        patient_item['name'] = patient.name

        query_list.append(patient_item)

    def check_query_list(self, query_list, patient):

        for patient_item in query_list:
            if patient_item['value'] == patient.email:
                return True

        return False
