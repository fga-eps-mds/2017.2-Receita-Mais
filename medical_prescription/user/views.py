from django.shortcuts import render
from .models import HealthProfessional
from .forms import HealthProfessionalForm, UserForm
from .models import User


def register_health_professional(request):
    user_form = UserForm(request.POST or None)
    hp_form = HealthProfessionalForm(request.POST or None)
    context = {
        'hp_form': hp_form,
        'user_form': user_form
    }

    if user_form.is_valid() and hp_form.is_valid():
        email = user_form.cleaned_data.get('email')
        password = user_form.cleaned_data.get('password')
        name = user_form.cleaned_data.get('name')
        sex = user_form.cleaned_data.get('sex')
        phone = user_form.cleaned_data.get('phone')
        date_of_birth = user_form.cleaned_data.get('date_of_birth')

        crm = hp_form.cleaned_data.get('crm')
        crm_state = hp_form.cleaned_data.get('crm_state')

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


def edit_health_professional(request):
    user_form = UserForm()
    hp_form = HealthProfessionalForm()
    context = {
        'hp_form': hp_form,
        'user_form': user_form
    }

    return render(request, 'edit_health_professional.html', context)


def delete_health_professional(request):
    return render(request, 'delete_health_professional.html')
