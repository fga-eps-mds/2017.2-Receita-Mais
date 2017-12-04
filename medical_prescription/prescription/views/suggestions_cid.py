# standard library
import json

# django
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# local django
from user.decorators import is_health_professional
from prescription.models import Prescription


class SuggestionsCid(View):
    """
    Responsible for obtaining suggested prescriptions to the CID.
    """

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(SuggestionsCid, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            id_cid = request.POST.get('id', False)
            prescriptions = Prescription.objects.filter(cid=id_cid,
                                                        health_professional=request.user.healthprofessional)[:5]

            result = dict()
            list_prescription = []
            result['status'] = "success"

            # Load dictionary with prescriptions.
            for prescription in prescriptions:
                prescription_item = {}
                prescription_item['id'] = prescription.id
                prescription_item['cid'] = prescription.cid.description
                prescription_item['medicines'] = self.get_medicines(prescription)
                prescription_item['exams'] = self.get_exams(prescription)
                prescription_item['recommendations'] = self.get_recomendations(prescription)
                if hasattr(prescription, 'patientprescription'):
                    prescription_item['patient'] = prescription.patientprescription.patient.name
                else:
                    prescription_item['patient'] = prescription.nopatientprescription.patient
                list_prescription.append(prescription_item)

            result['data'] = list_prescription

            mimetype = 'application/json'
            return HttpResponse(json.dumps(result), mimetype)
        else:
            # Nothing to do.
            pass

    # Get medicines related with some prescription.
    def get_medicines(self, prescription):
        list_medicines = []
        for medicine in prescription.medicines.all()[:5]:
            medicine_item = {}
            medicine_item['name'] = medicine.name
            list_medicines.append(medicine_item)

        for medicine in prescription.manipulated_medicines.all():
            medicine_item = {}
            medicine_item['name'] = medicine.recipe_name
            list_medicines.append(medicine_item)

        return list_medicines

    # Get exams related with some prescription.
    def get_exams(self, prescription):
        list_exams = []
        for exam in prescription.default_exams.all():
            exam_item = {}
            exam_item['name'] = exam.description
            list_exams.append(exam_item)

        for exam in prescription.custom_exams.all():
            exam_item = {}
            exam_item['name'] = exam.name
            list_exams.append(exam_item)

        return list_exams

    # Get recommendation related with some prescription.
    def get_recomendations(self, prescription):
        list_recommendations = []
        for recommendation in prescription.new_recommendations.all():
            recommendation_item = {}
            recommendation_item['name'] = recommendation.recommendation_description
            list_recommendations.append(recommendation_item)

        return list_recommendations
