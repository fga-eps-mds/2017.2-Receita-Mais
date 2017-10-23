from django.views.generic import View
from django.http import JsonResponse

from user.models import User


class AutoCompletePatient(View):
    """
    Responsible for getting patients similar to digits entered to help the user.
    """
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            search = request.GET.get('search', '')

            # TODO(Ronyell) Modifying User to Patiente.
            queryset = User.objects.filter(name__icontains=search)[:5]
            list = []

            # TODO(Ronyell) Change the required data.
            # Encapsulates in a json needed to be sent.
            for patient in queryset:
                list.append(patient.name)
            data = {
                'list': list,
            }
            print(list)
            return JsonResponse(data)
