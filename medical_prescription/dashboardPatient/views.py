# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Local Django imports
from user.decorators import is_patient


@login_required
@is_patient
def home(request):
    return render(request, 'patient_dashboard.html')
