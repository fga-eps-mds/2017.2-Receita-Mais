# Django
from django.views.generic import UpdateView
from django.urls import reverse_lazy

# Django Local
from exam.forms import UpdateCustomExamForm
from exam.models import CustomExam


class UpdateCustomExam(UpdateView):
        model = CustomExam
        form_class = UpdateCustomExamForm
        template_name = 'update_customexam.html'

        def get_success_url(self, **kwargs):
                return reverse_lazy('list_custom_exams')
