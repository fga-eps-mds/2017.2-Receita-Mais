
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import date

from chat.models import Message, Response
from chat.forms import CreateResponse


class SentMessageDetailView(DetailView, FormMixin):

    form_class = CreateResponse
    context_object_name = 'list'
    model = Message
    paginate_by = 40
    template_name = 'view_sent_message.html'

    def get_queryset(self):
        return self.model.objects.filter(user_from=self.request.user)

    def get_success_url(self):
        return reverse('view_sent_message', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(SentMessageDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CreateResponse(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        text = form.cleaned_data.get('text')

        response = Response()
        response.user_from = self.object.user_from
        response.user_to = self.object.user_to
        response.text = text
        response.dat = date.today()
        response.save()

        self.object.messages.add(response)

        return super(SentMessageDetailView, self).form_valid(form)
