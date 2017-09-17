from django.shortcuts import render
from .models import HealthProfessional
from .forms import HealthProfessionalForm


def register_health_professional(request):
    form = HealthProfessionalForm()
    context = {
        'form': form
    }
    return render(request, 'register_health_professional.html', context)


def view_health_professional(request):
    health_professionals = HealthProfessional.objects.all()
    context = {
        'health_professionals': health_professionals
    }
    return render(request, 'view_health_professional.html', context)


def edit_health_professional(request):
    return render(request, 'edit_health_professional.html')


def delete_health_professional(request):
    return render(request, 'delete_health_professional.html')
