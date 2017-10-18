from django.views.generic import View
from django.http import JsonResponse

from user.models import User


class AutoCompletePatient(View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            search = request.GET.get('search', '')
            # TODO(Ronyell) Modifying User to Patiente.
            queryset = User.objects.filter(name__icontains=search)[:5]
            list = []
            for patient in queryset:
                list.append(patient.name)
            data = {
                'list': list,
            }
            print(list)
            return JsonResponse(data)
