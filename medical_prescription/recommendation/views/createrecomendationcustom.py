from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from recommendation.models import CustomRecommendation
from recommendation.forms import CreateRecomendationCustomForm
from user.decorators import is_health_professional


class CustomRecommendationCreateView(FormView):
    form_class = CreateRecomendationCustomForm
    template_name = 'createcustomrecomendatiom.html'

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(CustomRecommendationCreateView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.get_request(request)
        if form.is_valid():
            description = form.cleaned_data.get('description')
            name = form.cleaned_data.get('name')
            user = request.user.healthprofessional

            health_professional_FK = user

            CustomRecommendation.objects.create(name=name, recommendation=description,
                                                health_professional=health_professional_FK,
                                                is_active=True)

            return redirect('/dashboard_health_professional/health_professional')

        return render(request, self.template_name, {'form': form})
