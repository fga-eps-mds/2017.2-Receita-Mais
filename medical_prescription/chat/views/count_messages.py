from django.views.generic import View
from django.http import JsonResponse

from chat.models import Message


class CountMessagesView(View):
    """
        Return a query of messages unread.
    """
    def get(self, request, *args, **kwargs):

        if request.is_ajax():

            queryset = Message.objects.filter(user_from=request.user, as_read=False)

            query_list = []

            for user in queryset:
                query_list.append(user.email)

            data = {
                'list': query_list,
                'list_len': len(query_list)
            }
            return JsonResponse(data)
