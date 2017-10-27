# Django
from django.shortcuts import render, redirect
from django.views.generic import FormView
from datetime import date

# Local Django
from chat.forms import CreateMessage
from chat.models import Message, Response
from user.models import User


class ComposeView(FormView):
    form_class = CreateMessage
    template_name = 'compose.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():

            text = form.cleaned_data.get('text')
            subject = form.cleaned_data.get('subject')
            user_to_email = form.cleaned_data.get('user_to')
            user_from = request.user
            user_to = User.objects.get(email=user_to_email)

            message = Message()
            message.subject = subject
            message.user_to = user_to
            message.user_from = user_from
            message.date = date.today()

            response = Response()
            response.user_from = user_from
            response.user_to = user_to
            response.text = text
            response.dat = date.today()
            response.save()

            message.save()

            message.messages.add(response)

            return redirect('/dashboard_health_professional/health_professional')

        return render(request, self.template_name, {'form': form})
