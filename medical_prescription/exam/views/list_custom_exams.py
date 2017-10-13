from django.views.generic import ListView
from exam.models import CustomExam
from django.contrib.auth.decorators import login_required

login_required()


class ListCustomExams(ListView):
    '''
    Query and list objects Medication.
    '''

    template_name = 'list_custom_exams.html'
    context_object_name = 'list_custom_exam'
    model = CustomExam
    paginate_by = 20

    # Get 20 queries of objects Medication.
    def get_queryset(self):
        return self.model.objects.all()
