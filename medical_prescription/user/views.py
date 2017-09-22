from django.shortcuts import render
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

from .forms import HealthProfessionalForm, UserForm, UpdateUserForm
from .models import HealthProfessional
from .models import User


def show_homepage(request):
    return render(request, 'home.html')


def register_health_professional(request):
    user_form = UserForm(request.POST or None)
    health_professional_form = HealthProfessionalForm(request.POST or None)
    context = {
        'health_professional_form': health_professional_form,
        'user_form': user_form
    }

    if user_form.is_valid() and health_professional_form.is_valid():
        email = user_form.cleaned_data.get('email')
        password = user_form.cleaned_data.get('password')
        name = user_form.cleaned_data.get('name')
        sex = user_form.cleaned_data.get('sex')
        phone = user_form.cleaned_data.get('phone')
        date_of_birth = user_form.cleaned_data.get('date_of_birth')

        crm = health_professional_form.cleaned_data.get('crm')
        crm_state = health_professional_form.cleaned_data.get('crm_state')

        User.objects.create_user(
            email=email, password=password, name=name,
            sex=sex, date_of_birth=date_of_birth, phone=phone)

        user = User.objects.get(email=email)

        health_professional = HealthProfessional(
            user=user, crm=crm, crm_state=crm_state)

        health_professional.save()

    return render(request, 'register_health_professional.html', context)


def view_health_professional(request):
    health_professionals = HealthProfessional.objects.all()
    context = {
        'health_professionals': health_professionals
    }
    return render(request, 'view_health_professional.html', context)


class DeleteHealthProfessional(DeleteView):
    model = HealthProfessional
    success_url = reverse_lazy('view')
    template_name = 'health_professional_confirm_delete.html'


class UpdateHealthProfessional(UpdateView):
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy('view')
    template_name = 'edit_health_professional.html'
