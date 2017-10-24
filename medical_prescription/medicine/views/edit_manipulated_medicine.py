from django.views.generic import UpdateView
from medicine.models import ManipulatedMedicine
from medicine.forms import EditForm
from django.urls import reverse


class UpdateMedicine(UpdateView):
    '''
        Edit Medicine attributes with this class.
    '''

    sucess_url = 'list_all_medicines'
    model = ManipulatedMedicine
    template_name = 'edit_manipulated_medicine.html'
    form_class = EditForm

    # Redirect for list _medicine_by_health_professional.
    def get_success_url(self):
        return reverse(self.sucess_url)
