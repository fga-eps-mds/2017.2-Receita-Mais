from django.shortcuts import render


def register_health_professional(request):
    return render(request, 'register_health_professional.html')


def view_health_professional(request):
    return render(request, 'view_health_professional.html')


def edit_health_professional(request):
    return render(request, 'edit_health_professional.html')


def delete_health_professional(request):
    return render(request, 'delete_health_professional.html')
