# Django
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import date

# Local Django
from chat.forms import CreateMessage
from chat.models import Message
from user.models import User
from user.decorators import is_health_professional


class ComposeView(FormView):
    form_class = CreateMessage
    template_name = 'compose.html'

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
            text = form.cleaned_data.get('text')
            subject = form.cleaned_data.get('subject')
            user_to_email = form.cleaned_data.get('user_to')
            user_from = request.user
            user_to = User.objects.get(email=user_to_email)

            Message.objects.create(text=text, subject=subject,
                                   user_to=user_to, user_from=user_from, date=date.today())

            return redirect('/dashboard_health_professional/health_professional')

        return render(request, self.template_name, {'form': form})
