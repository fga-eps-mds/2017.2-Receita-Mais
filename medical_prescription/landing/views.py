# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from user.decorators import user_is_logged


@user_is_logged
def home(request):
    return render(request, 'landing.html')


def team_page(request):
    return render(request, 'team.html')
