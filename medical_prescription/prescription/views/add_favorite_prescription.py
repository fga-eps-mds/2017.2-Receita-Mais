# django
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# local django
from user.decorators import is_health_professional
from prescription.models import Prescription


class AddFavoritePrescription(View):

    """
    This class is responsible for make a prescription favorite.
    """

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def post(self, request, pk, *args, **kwargs):

        if request.method == 'POST':
            prescription = Prescription.objects.get(pk=pk)

            print("favorite")
            prescription.is_favorite = True

            prescription.save()

        return HttpResponseRedirect(reverse_lazy('list_prescription'))
