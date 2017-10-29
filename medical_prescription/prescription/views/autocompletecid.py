# standard library
import json

# django
from django.views.generic import View
from django.http import HttpResponse

# local django
from disease.models import Disease


class AutoCompleteCid(View):
    """
    Responsible for getting CIDs similar to digits entered to help the user.
    """

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            search = request.GET.get('term', '')
            queryset = Disease.objects.filter(description__icontains=search)[:5]
            list_disease = []

            # Encapsulates in a json needed to be sent.
            for disease in queryset:
                disease_item = {}
                disease_item['value'] = disease.description
                disease_item['name'] = disease.description
                disease_item['id'] = disease.id
                list_disease.append(disease_item)

            data = json.dumps(list_disease)
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)
