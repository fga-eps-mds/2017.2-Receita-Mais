from django.views.generic import UpdateView
from medication.models import Medication
from medication.forms import EditForm
from django.urls import reverse


class UpdateMedication(UpdateView):
    '''
        Edit Medication attributes with this class.
    '''

    sucess_url = 'list_medication'
    model = Medication
    template_name = 'edit_medication.html'
    form_class = EditForm

    def get_success_url(self):
        return reverse(self.sucess_url)
