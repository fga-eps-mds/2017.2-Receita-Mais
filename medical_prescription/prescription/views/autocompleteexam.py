# standard library
import json

# Django imports
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# local django
from user.decorators import is_health_professional
from exam.models import DefaultExam, CustomExam
from prescription import constants


class AutoCompleteExam(View):
    """
    Responsible for getting Exams similar to digits entered to help the user.
    """

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(AutoCompleteExam, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            search = request.GET.get('term', '')
            list_exams = []

            self.get_default_exams(search, list_exams)
            self.get_custom_exams(search, request.user, list_exams)

            data = json.dumps(list_exams)
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)

    def get_custom_exams(self, search, health_professional, list_exams):
        queryset = CustomExam.objects.filter(description__icontains=search,
                                             health_professional_FK=health_professional)[:5]

        # Encapsulates in a json needed to be sent.
        for custom_exam in queryset:
            custom_exam_item = {}
            custom_exam_item['value'] = self.parse_description(custom_exam.description)
            custom_exam_item['id'] = custom_exam.auto_increment_id
            custom_exam_item['type'] = 'custom_exam'
            custom_exam_item['description'] = self.parse_description(custom_exam.description)

            list_exams.append(custom_exam_item)

    def get_default_exams(self, search, list_exams):
        queryset = DefaultExam.objects.filter(description__icontains=search)[:5]

        # Encapsulates in a json needed to be sent.
        for default_exam in queryset:
            default_exam_item = {}
            default_exam_item['value'] = self.parse_description(default_exam.description)
            default_exam_item['id'] = default_exam.auto_increment_id
            default_exam_item['type'] = 'default_exam'
            default_exam_item['description'] = self.parse_description(default_exam.description)

            list_exams.append(default_exam_item)

    # Print only the first 175 characters of the exam description.
    def parse_description(self, description):
        if len(description) > constants.MAX_LENGTH_DESCRIPTION_AUTOCOMPLETE:
            return description[:175] + '...'
        else:
            return description
