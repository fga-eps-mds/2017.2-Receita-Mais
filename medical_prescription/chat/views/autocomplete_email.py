from django.views.generic import View
from django.http import JsonResponse

from user.models import User


class AutoCompleteEmail(View):
    """
    Return a query of email users.
    """
    def get(self, request, *args, **kwargs):

        if request.is_ajax():

            search = request.GET.get('search', '')
            queryset = User.objects.filter(email__icontains=search)[:5]
            query_list = []

            for user in queryset:
                query_list.append(user.email)

            data = {
                'list': query_list,
            }
            return JsonResponse(data)
