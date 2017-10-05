# Django
from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.generic import FormView

# Local Django
from user.forms import UserLoginForm


class LoginView(FormView):
    '''
    Render and log user.
    '''

    form_class = UserLoginForm
    template_name_patient = 'login_patient.html'
    template_name_healthProfessional = 'login_healthprofessional.html'
    template_name = ''

    # TODO(Felipe) Renderizar o template de acordo com o tipo de Usuário
    # Render the login page.
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)

        if(request.path == '/user/login_healthprofessional/'):
            return render(request, self.template_name_healthProfessional, {'form': form})
        else:
            return render(request, self.template_name_patient, {'form': form})

    # Login user.
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

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
                return render(request, self.template_name, {'form': form, 'message': message})
        else:
            return render(request, self.template_name, {'form': form})

    # Login valid user.
    def user_authentication(self, request, user):
        if user.is_active:

            # TODO(Felipe) Redirecionar a página da acordo com o tipo de usuário
            auth.login(request, user)
            return redirect('/dashboardHealthProfessional/health_professional')
