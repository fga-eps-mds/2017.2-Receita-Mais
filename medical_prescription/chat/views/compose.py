# Django
from django.shortcuts import render, redirect
from django.views.generic import FormView
from datetime import date
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local Django
from chat.forms import CreateMessage
from chat.models import Message, Response
from user.models import User
from user.decorators import is_health_professional


@method_decorator(login_required, name='dispatch')
@method_decorator(is_health_professional, name='dispatch')
class ComposeView(FormView):
    """
    Create a Message.
    """

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
        form = self.form_class(request.POST, request.FILES)
        pk = self.request.user.pk
        form.get_pk(pk)

        # Validanting form.
        if form.is_valid():

            text = form.cleaned_data.get('text')
            subject = form.cleaned_data.get('subject')
            user_to_email = form.cleaned_data.get('user_to')
            user_from = request.user
            user_to = User.objects.get(email=user_to_email)

            # Create a Message
            message = Message()
            message.subject = subject
            message.user_to = user_to
            message.user_from = user_from
            message.date = date.today()

            response = Response(files=request.FILES.get('files', None))

            if response.files:
                response.file_name = response.files.name

            response.user_from = user_from
            response.user_to = user_to
            response.text = text
            response.dat = date.today()
            response.save()
            message.save()

            message.messages.add(response)

            return redirect('/dashboard_health_professional/health_professional')

        return render(request, self.template_name, {'form': form})
