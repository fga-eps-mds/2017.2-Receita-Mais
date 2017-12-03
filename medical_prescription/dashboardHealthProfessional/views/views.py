# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime, timedelta

# Django imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Local Django imports
from user.decorators import is_health_professional
from prescription.models import Prescription


@login_required
@is_health_professional
def home(request):
    health_professional = request.user.healthprofessional
    one_week_ago = datetime.today() - timedelta(days=7)
    prescription_quantity = Prescription.objects.filter(date__gte=one_week_ago,
                                                        health_professional=health_professional).count()

    last_prescriptions = Prescription.objects.filter(health_professional=health_professional).order_by('-id')[:6]

    print(last_prescriptions)
    return render(request, 'healthprofessional.html', {'prescription_quantity': prescription_quantity,
                                                       'last_prescriptions': last_prescriptions})
