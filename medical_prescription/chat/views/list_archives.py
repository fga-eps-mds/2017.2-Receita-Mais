# Django imports
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local Django
from chat.models import Response
from user.decorators import is_patient


class ListArchives(ListView):
    '''
    Query and list archives.
    '''

    template_name = 'list_sent_archives.html'
    context_object_name = 'list_archive'
    model = Response
    paginate_by = 20

    @method_decorator(login_required)
    @method_decorator(is_patient)
    def dispatch(self, *args, **kwargs):
        return super(ListArchives, self).dispatch(*args, **kwargs)

    # Get 20 queries of Archives objects.
    def get_queryset(self):
        return self.model.objects.filter(user_from=self.request.user)
