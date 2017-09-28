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
    template_name = 'login.html'

    # Render the login page.
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

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
            auth.login(request, user)
            return redirect('/dashboard/health_professional')
