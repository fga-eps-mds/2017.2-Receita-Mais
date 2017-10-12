from django.views.generic import ListView
from exam.models import Exam


class ListExams(ListView):
    '''
    Query and list objects Medication.
    '''

    template_name = 'list_exams.html'
    context_object_name = 'list_exam'
    model = Exam
    paginate_by = 20

    # Get 20 queries of objects Medication.
    def get_query_set(self, request):
        return self.model.objects.all()
