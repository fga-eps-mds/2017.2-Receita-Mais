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


class SugestionsCid(View):
    """
    Responsible for obtaining suggested prescriptions to the CID.
    """

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(SugestionsCid, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            id_cid = request.POST.get('id', False)
            prescriptions = Prescription.objects.filter(cid=id_cid, health_professional=request.user.healthprofessional)

            result = dict()
            list_prescription = []
            result['status'] = "success"

            for prescription in prescriptions:
                prescription_item = {}
                prescription_item['id'] = prescription.id
                prescription_item['cid'] = prescription.cid.description
                list_prescription.append(prescription_item)

            result['data'] = list_prescription

            mimetype = 'application/json'
            return HttpResponse(json.dumps(result), mimetype)
