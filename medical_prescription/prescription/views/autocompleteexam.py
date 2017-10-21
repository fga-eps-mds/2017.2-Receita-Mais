from django.views.generic import View
from django.http import JsonResponse

from exam.models import Exam


class AutoCompleteExam(View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            search = request.GET.get('search', '')
            queryset = Exam.objects.filter(description__icontains=search)[:5]
            list = []
            for exam in queryset:
                exam_item = {}
                exam_item['value'] = exam.description
                list.append(exam_item)
            data = {
                'list': list,
            }
            print(list)
            return JsonResponse(data)
