# standard library
import logging

# Django
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib import messages
from django.utils.decorators import method_decorator

# Local Django
from user.models import HealthProfessional
from user.forms import HealthProfessionalForm
from user import constants
from user.views import ConfirmAccountView
from user.decorators import user_is_logged

# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class RegisterHealthProfessionalView(FormView):
    form_class = HealthProfessionalForm
    template_name = 'register_health_professional.html'

    @method_decorator(user_is_logged)
    def get(self, request, *args, **kwargs):
        logger.debug("Start get method.")
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        logger.debug("Start post method.")
        form = self.form_class(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            name = form.cleaned_data.get('name')
            sex = form.cleaned_data.get('sex')
            phone = form.cleaned_data.get('phone')
            date_of_birth = form.cleaned_data.get('date_of_birth')

            crm = form.cleaned_data.get('crm')
            crm_state = form.cleaned_data.get('crm_state')

            specialty_first = form.cleaned_data.get('specialty_first')
            specialty_second = form.cleaned_data.get('specialty_second')
            HealthProfessional.objects.create_user(email=email, password=password, name=name,
                                                   sex=sex, date_of_birth=date_of_birth,
                                                   phone=phone, crm=crm, crm_state=crm_state,
                                                   specialty_first=specialty_first,
                                                   specialty_second=specialty_second)

            ConfirmAccountView.activate_account_request(email)
            messages.success(
                request, 'Registro Realizado!Um email foi enviado com seu link para ativação!', extra_tags='alert')

            logger.debug("Exit post method - Successful user registration.")
            return redirect('/')

        logger.debug("Exit post method - Not successful user registration.")
        return render(request, self.template_name, {'form': form})
