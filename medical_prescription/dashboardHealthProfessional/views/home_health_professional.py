# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime, timedelta

# Django imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator

# local django
from user.decorators import is_health_professional
from prescription.models import Prescription


class HomeHealthProfessional(View):
    """
    Renders the home page (dashboard) of the health professional.
    """
    template_name = 'healthprofessional.html'

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(HomeHealthProfessional, self).dispatch(*args, **kwargs)

    def get(self, request):
        health_professional = request.user.healthprofessional
        one_week_ago = datetime.today() - timedelta(days=7)

        # Set initial date first hour
        week_ago = datetime(one_week_ago.year, one_week_ago.month, one_week_ago.day)
        prescription_quantity = Prescription.objects.filter(date__gte=week_ago,
                                                            health_professional=health_professional).count()

        # Get six latest prescriptions
        latest_prescriptions = Prescription.objects.filter(health_professional=health_professional).order_by('-id')[:6]

        return render(request, self.template_name, {'prescription_quantity': prescription_quantity,
                                                    'last_prescriptions': latest_prescriptions})
