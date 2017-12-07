# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime, timedelta

# Django imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator

# local django
from user.decorators import is_patient
from prescription.models import PatientPrescription
from chat.models import Message


class HomePatient(View):
    """
    Renders the home page (dashboard) of the health professional.
    """
    template_name = 'patient_dashboard.html'

    @method_decorator(login_required)
    @method_decorator(is_patient)
    def dispatch(self, *args, **kwargs):
        return super(HomePatient, self).dispatch(*args, **kwargs)

    def get(self, request):
        patient = request.user.patient
        one_week_ago = datetime.today() - timedelta(days=7)

        # Set initial date first hour
        week_ago = datetime(one_week_ago.year, one_week_ago.month, one_week_ago.day)
        prescription_quantity = PatientPrescription.objects.filter(date__gte=week_ago,
                                                                   patient=patient).count()

        # Get six latest prescriptions
        latest_prescriptions = PatientPrescription.objects.filter(patient=patient).order_by('-id')[:6]

        # Get six latest messages
        latest_messages = Message.objects.filter(user_to=patient).order_by('-id')[:6]

        return render(request, self.template_name, {'prescription_quantity': prescription_quantity,
                                                    'last_prescriptions': latest_prescriptions,
                                                    'latest_messages': latest_messages})
