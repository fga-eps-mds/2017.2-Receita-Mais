from django.views.generic import UpdateView
from medication.models import Medication


class UpdateMedication(UpdateView):
    '''
        Edit Medication attributes with this class.
    '''

    model = Medication

    # Fields of eidt Form.
    fields = ['name',
              'active_ingredient',
              'laboratory',
              'description',
              'is_restricted']

    template_name = 'edit_medication'
