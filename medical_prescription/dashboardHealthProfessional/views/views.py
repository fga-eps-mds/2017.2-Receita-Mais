# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Local Django imports
from user.decorators import is_health_professional


@login_required
@is_health_professional
def home(request):
    return render(request, 'healthprofessional.html')
