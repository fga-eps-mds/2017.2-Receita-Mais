# Django
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required

# Local Django
from exam.models import CustomExam
from exam.forms import CreateCustomExams


login_required()


class CreateCustomExamsView(FormView):
    form_class = CreateCustomExams
    template_name = 'create_custom_exam.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        custom_exam_form = self.form_class(request.POST)

        if custom_exam_form.is_valid():
            description = custom_exam_form.cleaned_data.get('description')
            health_professional_FK = request.user.pk

            CustomExam.objects.create_user(description=description, health_professional_FK=health_professional_FK)

        return render(request, self.template_name, {'form': custom_exam_form})
