# Django
from django.views.generic import UpdateView
from django.shortcuts import render, redirect
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

        def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            form = self.form_class(request.POST)
            pk = self.object.pk
            form.get_pk(pk)

            if form.is_valid():
                description = form.cleaned_data.get('description')
                name = form.cleaned_data.get('name')

                CustomExam.objects.filter(pk=pk).update(name=name, description=description)

                return redirect('/exam/list_custom_exams/')

            return render(request, self.template_name, {'form': form})
