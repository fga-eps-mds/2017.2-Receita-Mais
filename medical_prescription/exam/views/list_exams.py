from django.views.generic import ListView
from exam.models import DefaultExam
from django.contrib.auth.decorators import login_required

login_required()


class ListExams(ListView):
    '''
    Query and list objects Medication.
    '''

    template_name = 'list_exams.html'
    context_object_name = 'list_exam'
    model = DefaultExam
    paginate_by = 20

    # Get 20 queries of objects Medication.
    def get_queryset(self):
        return self.model.objects.all()
