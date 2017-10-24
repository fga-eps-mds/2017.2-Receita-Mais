from django.views.generic import ListView

from medicine.models import ManipulatedMedicine


class ListManipulatedMedicinenByHealthProfessional(ListView):
    '''
        View for listing medications created by the Health Professional.
    '''

    template_name = 'list_manipulated_medicines.html'
    context_object_name = 'list_medicines'
    model = ManipulatedMedicine
    paginate_by = 20

    # Listing objects created by the logged Health Professional.
    def get_queryset(self):
        return self.model.objects.filter(health_professional=self.request.user)
