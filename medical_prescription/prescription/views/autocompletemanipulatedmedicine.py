import json

from django.views.generic import View
from django.http import HttpResponse

from medicine.models import (
                            ManipulatedMedicine
                            )
from prescription import constants


class AutoCompleteManipulatedMedicine(View):
    """
    Responsible for getting Medicines similar to digits entered to help the user.
    """

    # Print only the first 175 characters of the composition.
    def parse_composition(self, composition):
        if len(composition) > constants.MAX_LENGTH_COMPOSITION_AUTOCOMPLETE:
            return composition[:175] + '...'
        else:
            return composition

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            search = request.GET.get('term', '')

            queryset = ManipulatedMedicine.objects.filter(recipe_name__icontains=search)[:5]
            list_manipulated_medicines = []

            # Encapsulates in a json needed to be sent.
            for manipulated_medicine in queryset:
                manipulated_medicine_item = {}
                manipulated_medicine_item['value'] = manipulated_medicine.recipe_name
                manipulated_medicine_item['id'] = manipulated_medicine.id
                manipulated_medicine_item['category'] = 'manipulated_medicine'
                manipulated_medicine_item['composition'] = self.parse_composition(manipulated_medicine.composition)

                list_manipulated_medicines.append(manipulated_medicine_item)

            data = json.dumps(list_manipulated_medicines)
            print (data)
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)
