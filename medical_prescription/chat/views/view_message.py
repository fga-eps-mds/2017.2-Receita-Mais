# Django
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from datetime import date
from django.core import paginator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render

# Local Django
from chat.models import Message, Response
from chat.forms import CreateResponse


@method_decorator(login_required, name='dispatch')
class MessageDetailView(DetailView, FormMixin):
    """
    Class for detail Message from the User.
    """

    form_class = CreateResponse
    context_object_name = 'list'
    model = Message
    template_name = 'view_message_patient.html'

    # Return a query of Message from the user.
    def get_queryset(self):
        return self.model.objects.filter(user_to=self.request.user)

    # Returns all messages in chat.
    def get_context_data(self, **kwargs):
        context = super(MessageDetailView, self).get_context_data(**kwargs)

        messages_page = self.request.GET.get('page')
        messages = Response.objects.filter(message__id=context['object'].id)

        messages_list = messages[::-1]

        messages_paginator = paginator.Paginator(messages_list, 10)

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

        context['img_from'] = self.object.user_from.image_profile.url
        context['img_to'] = self.object.user_to.image_profile.url
        context['my_user'] = request.user

        # Get the last element of messages.
        last_element = self.object.messages.all().last()

        # Mark all responses with read = True.
        if(last_element.user_to.email == request.user.email):
            for message in self.object.messages.filter(as_read=False):
                message.as_read = True
                message.save()

        # Save the Message.
        self.object.save()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CreateResponse(request.POST, request.FILES)

        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, request):
        text = form.cleaned_data.get('text')

        # Get elements of Form and save the response.
        response = Response(files=request.FILES.get('files', None))

        if response.files:
            response.file_name = response.files.name

        response.user_from = self.object.user_to
        response.user_to = self.object.user_from
        response.text = text
        response.dat = date.today()

        if(response.user_from is request.user):
            response.as_read = True
        else:
            # Nothing to do.
            pass

        response.save()

        self.object.messages.add(response)

        return super(MessageDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('view_message_patient', kwargs={'pk': self.object.pk})
