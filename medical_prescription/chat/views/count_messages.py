import json

from django.views.generic import View
from django.http import HttpResponse

from chat.models import Response


class CountMessagesView(View):
    """
        Return a query of messages unread.
    """
    def post(self, request, *args, **kwargs):

        if request.is_ajax():

            queryset = Response.objects.filter(user_to=request.user, as_read=False)

            query_list = []

            for message in queryset:
                message_item = {}
                message_item['text'] = message.text
                message_item['user_from'] = str(message.user_from.name)
                query_list.append(message_item)

            data = json.dumps(query_list)

            mimetype = 'application/json'
            return HttpResponse(json.dumps(data), mimetype)
