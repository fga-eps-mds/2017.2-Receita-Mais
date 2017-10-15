from django.views.generic import UpdateView
from medication.models import Medication
from medication.forms import EditForm


class UpdateMedication(UpdateView):
    '''
        Edit Medication attributes with this class.
    '''

    model = Medication
    template_name = 'edit_medication.html'
    form_class = EditForm
