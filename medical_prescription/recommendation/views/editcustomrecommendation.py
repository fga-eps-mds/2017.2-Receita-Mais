# Django imports
from django.views.generic import UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Django Local imports
from exam.forms import UpdateCustomRecommendationForm
from exam.models import CustomRecommendation
from user.decorators import is_health_professional


class UpdateCustomRecommendation(UpdateView):
        model = CustomRecommendation
        form_class = UpdateCustomRecommendationForm
        template_name = 'update_customrecommendation.html'

        @method_decorator(login_required)
        @method_decorator(is_health_professional)
        def dispatch(self, *args, **kwargs):
            return super(UpdateCustomRecommendation, self).dispatch(*args, **kwargs)

        def get_success_url(self, **kwargs):
                return reverse_lazy('list_custom_exams')

        def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            form = self.form_class(request.POST)
            pk = self.object.pk
            form.get_pk(pk)

            if form.is_valid():
                recommendation = form.cleaned_data.get('recommendation')
                name = form.cleaned_data.get('name')

                CustomRecommendation.objects.filter(pk=pk).update(name=name, recommendation=recommendation)

                return redirect('/exam/update_custom_recommendation/')

            return render(request, self.template_name, {'form': form})
