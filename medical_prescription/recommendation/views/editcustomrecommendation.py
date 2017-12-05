# Django imports
from django.views.generic import UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Django Local imports
from recommendation.forms import UpdateCustomRecommendationForm
from recommendation.models import CustomRecommendation
from user.decorators import is_health_professional


class UpdateCustomRecommendation(UpdateView):
    """
    Update Custom recommendation class.
    """
    model = CustomRecommendation
    form_class = UpdateCustomRecommendationForm
    template_name = 'update_customrecommendation.html'

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(UpdateCustomRecommendation, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST or None)
        pk = self.object.pk
        form.get_pk(pk)

        if form.is_valid():
            description = form.cleaned_data.get('recommendation')
            name = form.cleaned_data.get('name')

            CustomRecommendation.objects.filter(pk=pk).update(name=name, recommendation=description)

            return redirect('/exam/update_custom_recommendation/')
        else:
            return render(request, self.template_name, {'form': form})
