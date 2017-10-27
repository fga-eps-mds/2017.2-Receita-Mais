import json

from django.views.generic import View
from django.http import HttpResponse

from exam.models import CustomExam


class AutoCompleteExam(View):
    """
    Responsible for getting Exams similar to digits entered to help the user.
    """
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            search = request.GET.get('term', '')

            # TODO(Ronyell) Change logic to all exam.
            queryset = CustomExam.objects.filter(name__icontains=search)[:5]
            list_exam = []

            # TODO(Ronyell) Change the required data.
            # Encapsulates in a json needed to be sent.
            for exam in queryset:
                exam_item = {}
                exam_item['value'] = exam.name
                exam_item['id'] = exam.auto_increment_id
                exam_item['description'] = exam.description
                exam_item['name'] = exam.name

                list_exam.append(exam_item)
            data = json.dumps(list_exam)
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)
