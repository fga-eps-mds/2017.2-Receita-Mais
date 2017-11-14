# django
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# local django
from user.decorators import is_health_professional
from prescription.models import Prescription


class AddFavoritePrescription(View):

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def favorite_prescription(self, request, pk):
        prescription = Prescription.objects.get(pk=pk)
        prescription.is_favorite = True
        prescription.save()
