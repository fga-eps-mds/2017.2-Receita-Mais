# Django imports
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local Django imports
from exam.models import CustomExam
from exam.forms import CreateCustomExams
from user.models import HealthProfessional
from user.decorators import is_health_professional


class CreateCustomExamsView(FormView):
    form_class = CreateCustomExams
    template_name = 'create_custom_exams.html'

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(CreateCustomExamsView, self).dispatch(*args, **kwargs)

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            description = form.cleaned_data.get('description')
            name = form.cleaned_data.get('name')
            user = request.user.healthprofessional

            health_professional_FK = user

            CustomExam.objects.create(name=name, description=description,
                                      health_professional_FK=health_professional_FK)

            return redirect('/dashboard_health_professional/health_professional')

        return render(request, self.template_name, {'form': form})
