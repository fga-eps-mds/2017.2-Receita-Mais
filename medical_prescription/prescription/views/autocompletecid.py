from django.views.generic import View
from django.http import JsonResponse

from disease.models import Disease


class AutoCompleteCid(View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            search = request.GET.get('search', '')
            queryset = Disease.objects.filter(description__icontains=search)[:5]
            list = []
            for disease in queryset:
                list.append(disease.description)
            data = {
                'list': list,
            }
            print(list)
            return JsonResponse(data)
