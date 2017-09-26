# Django
from django.views.generic import TemplateView


class ShowHomePageView(TemplateView):
    template_name = 'home.html'
