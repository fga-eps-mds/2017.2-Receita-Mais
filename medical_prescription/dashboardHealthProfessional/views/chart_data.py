# standard library
import json
from datetime import datetime, timedelta

# django
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# local django
from user.decorators import is_health_professional
from prescription.models import Prescription
from dashboardHealthProfessional import constants


class ChartData(View):
    """
    Responsible for obtaining data for the chart.
    """

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(ChartData, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            list_date = []
            health_professional = request.user.healthprofessional

            for count in range(7, -1, -1):
                chart_item = {}
                date_ago = datetime.today() - timedelta(days=count)

                # Set initial date first hour
                actual_date = datetime(date_ago.year, date_ago.month, date_ago.day)
                prescription_count = Prescription.objects.filter(date__year=actual_date.year,
                                                                 date__month=actual_date.month,
                                                                 date__day=actual_date.day,
                                                                 health_professional=health_professional).count()

                # Checks whether the date in question is the current date.
                if count:
                    chart_item['name'] = actual_date.strftime('%A')
                else:
                    chart_item['name'] = constants.TODAY

                chart_item['quantity'] = prescription_count
                list_date.append(chart_item)

            result = json.dumps(list_date)
            mimetype = 'application/json'
            return HttpResponse(result, mimetype)
