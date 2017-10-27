# Django imports
from django.views.generic import ListView
from exam.models import DefaultExam
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local Django imports
from exam.models import Exam
from user.decorators import is_health_professional


class ListExams(ListView):
    '''
    Query and list objects Medication.
    '''

    template_name = 'list_exams.html'
    context_object_name = 'list_exam'
    model = DefaultExam
    paginate_by = 20

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(ListExams, self).dispatch(*args, **kwargs)

    # Get 20 queries of objects Medication.
    def get_queryset(self):
        return self.model.objects.all()
