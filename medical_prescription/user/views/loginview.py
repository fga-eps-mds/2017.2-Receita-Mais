# standard library
import logging

# Django
from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.generic import FormView
from django.utils.decorators import method_decorator

# Local Django
from user.models import HealthProfessional
from user.forms import UserLoginForm
from user import constants
from user.decorators import user_is_logged

# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class LoginView(FormView):
    '''
    Render and log user.
    '''

    form_class = UserLoginForm
    template_name = ''
    dashboard_name = ''

    # Render the login page.
    @method_decorator(user_is_logged)
    def get(self, request, *args, **kwargs):
        logger.debug("Start get method.")
        form = self.form_class(initial=self.initial)

        self.set_template_name(request)

        return render(request, self.template_name, {'form': form})

    # Login user.
    def post(self, request, *args, **kwargs):
        logger.debug("Start post method.")
        form = self.form_class(request.POST)

        self.set_template_name(request)

        # Authenticate user.
        if form.is_valid():
            user = auth.authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                return self.user_authentication(request, user)
            else:
                message = 'O Usuário não foi encontrado em nossa base de dados.'
                logger.debug("Exit post method.")
                return render(request, self.template_name, {'form': form, 'message': message})
        else:
            logger.debug("Exit post method.")
            return render(request, self.template_name, {'form': form})

    # Define template and dashboard url
    def set_template_name(self, request):
        if "healthprofessional" in request.path:

            self.template_name = 'login_healthprofessional.html'
            self.dashboard_name = '/dashboard_health_professional/health_professional'
        else:
            self.template_name = 'login_patient.html'
            self.dashboard_name = '/dashboard_patient/patient'

    # Login valid user.
    def user_authentication(self, request, user):
        if user.is_active:

            # TODO(Felipe) Redirect for specify user.
            auth.login(request, user)
            return redirect(self.dashboard_name)
