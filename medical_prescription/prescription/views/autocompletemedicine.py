# standard library
import json

# django
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# local django
from user.decorators import is_health_professional
from medicine.models import (ManipulatedMedicine,
                             Medicine
                             )
from prescription import constants


class AutoCompleteMedicine(View):
    """
    Responsible for getting Medicines similar to digits entered to help the user.
    """
    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(AutoCompleteMedicine, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            search = request.GET.get('term', '')
            list_medicines = []

            self.get_medicines(search, list_medicines)
            self.get_manipulated_medicines(search, request.user, list_medicines)

            data = json.dumps(list_medicines)
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)

    def get_manipulated_medicines(self, search, health_professional, list_medicines):
        queryset = ManipulatedMedicine.objects.filter(recipe_name__icontains=search,
                                                      health_professional=health_professional)[:5]

        # Encapsulates in a json needed to be sent.
        for manipulated_medicine in queryset:
            manipulated_medicine_item = {}
            manipulated_medicine_item['value'] = manipulated_medicine.recipe_name
            manipulated_medicine_item['id'] = manipulated_medicine.id
            manipulated_medicine_item['type'] = 'manipulated_medicine'
            manipulated_medicine_item['description'] = self.parse_description(manipulated_medicine.composition)

            list_medicines.append(manipulated_medicine_item)

    def get_medicines(self, search, list_medicines):
        queryset = Medicine.objects.filter(name__icontains=search)[:5]

        # Encapsulates in a json needed to be sent.
        for medicine in queryset:
            medicine_item = {}
            medicine_item['value'] = medicine.name
            medicine_item['id'] = medicine.id
            medicine_item['type'] = 'medicine'
            medicine_item['description'] = self.parse_description(medicine.description)

            list_medicines.append(medicine_item)

    # Print only the first 175 characters of the composition.
    def parse_description(self, description):
        if len(description) > constants.MAX_LENGTH_DESCRIPTION_AUTOCOMPLETE:
            return description[:175] + '...'
        else:
            return description
