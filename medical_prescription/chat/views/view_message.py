# Django
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from datetime import date
from django.core import paginator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local Django
from chat.models import Message, Response
from chat.forms import CreateResponse

from django.shortcuts import render_to_response


@method_decorator(login_required, name='dispatch')
class MessageDetailView(DetailView, FormMixin):
    """
    Class for detail Message from the User.
    """

    form_class = CreateResponse
    context_object_name = 'list'
    model = Message

    # Return a query of Message from the user.
    def get_queryset(self):
        return self.model.objects.filter(user_to=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(MessageDetailView, self).get_context_data(**kwargs)

        messages_page = self.request.GET.get('page')
        messages = Response.objects.filter(message__id=context['object'].id)
        messages_paginator = paginator.Paginator(messages, 15)

        try:
            messages_page_object = messages_paginator.page(messages_page)
        except (paginator.PageNotAnInteger, paginator.EmptyPage):
            messages_page_object = messages_paginator.page(1)

        context['form'] = self.get_form()
        context['messages'] = messages_page_object
        return context

    def get(self, request, *args, **kwargs):
        self.object = Message.objects.get(pk=self.kwargs['pk'])

        context = self.get_context_data()

        self.object.as_read = True
        self.object.save()

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CreateResponse(request.POST, request.FILES)

        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, request):
        text = form.cleaned_data.get('text')

        response = Response()
        response = Response(files=request.FILES.get('files', None))
        response.user_from = self.object.user_to
        response.user_to = self.object.user_from
        response.text = text
        response.dat = date.today()
        response.save()

        self.object.messages.add(response)

        return super(MessageDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('view_message_patient', kwargs={'pk': self.object.pk})
