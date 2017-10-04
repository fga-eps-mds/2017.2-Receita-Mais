# Django
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib import messages


# Local Django
from user.models import HealthProfessional
from user.forms import HealthProfessionalForm


class RegisterHealthProfessionalView(FormView):
    form_class = HealthProfessionalForm
    template_name = 'register_health_professional.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
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

            HealthProfessional.objects.create_user(email=email, password=password, name=name,
                                                   sex=sex, date_of_birth=date_of_birth,
                                                   phone=phone, crm=crm, crm_state=crm_state)

            messages.success(
                request, 'Registro Realizado!Um email foi enviado com seu link para ativação!', extra_tags='alert')

            return redirect('/')

        return render(request, self.template_name, {'form': form})
