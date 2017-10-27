
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.shortcuts import render, redirect
from datetime import date

from chat.models import Message, Response
from chat.forms import CreateMessage


class MessageDetailView(DetailView, FormMixin):

    template_name = "view_message.html"
    form_class = CreateMessage

    context_object_name = 'list'
    model = Message
    paginate_by = 40

    def get_queryset(self):
        return self.model.objects.filter(user_to=self.request.user)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            text = form.cleaned_data.get('text')

            response = Response()
            response.user_from = self.object.user_from
            response.user_to = self.object.user_to
            response.text = text
            response.dat = date.today()
            response.save()

            self.object.save()

            self.object.messages.add(response)

            return redirect('/dashboard_health_professional/health_professional')

        return render(request, self.template_name, {'form': form})
