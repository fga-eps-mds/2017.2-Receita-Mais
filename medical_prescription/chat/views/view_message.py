# Django
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from datetime import date
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
    paginate_by = 40

    # Return a query of Message from the user.
    def get_queryset(self):
        return self.model.objects.filter(user_to=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(MessageDetailView, self).get_context_data(**kwargs)
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
        response.user_from = self.object.user_to
        response.user_to = self.object.user_from
        response.text = text
        response.dat = date.today()
        response.save()

        self.object.messages.add(response)

        return super(MessageDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('view_message_patient', kwargs={'pk': self.object.pk})
