# Django
from django.shortcuts import render, redirect
from django.views.generic import FormView
from datetime import date
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local Django
from prescription.forms import PatternForm
from prescription.models import Pattern
from user.decorators import is_health_professional


@method_decorator(login_required, name='dispatch')
@method_decorator(is_health_professional, name='dispatch')
class CreatePatternView(FormView):
    """
    Create a prescription Model.
    """

    form_class = PatternForm
    template_name = 'create_prescription_model.html'

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        # Validanting form.
        if form.is_valid():
            user_creator = request.user

            name = form.cleaned_data.get('name')
            header = form.cleaned_data.get('header')
            footer = form.cleaned_data.get('footer')
            clinic = form.cleaned_data.get('clinic')

            font = form.cleaned_data.get('font')
            font_size = form.cleaned_data.get('font_size')
            pagesize = form.cleaned_data.get('pagesize')

            # Create a Prescription type
            pattern_instance = Pattern()
            pattern_instance = Pattern(logo=request.FILES.get('logo', None))
            pattern_instance.user_creator = user_creator
            pattern_instance.name = name
            pattern_instance.header = header
            pattern_instance.footer = footer
            pattern_instance.clinic = clinic
            pattern_instance.font = font
            pattern_instance.font_size = font_size
            pattern_instance.pagesize = pagesize
            pattern_instance.date = date.today()
            pattern_instance.save()

            return redirect('/dashboard_health_professional/health_professional')

        return render(request, self.template_name, {'form': form})
