from django.views.generic import ListView
from user.models import AssociatedHealthProfessionalAndPatient
from django.contrib.auth.decorators import login_required

login_required()


# This class is responsible for list all patients who are related with the
# request health professional.
class ListLinkedPatientsView(ListView):

    template_name = 'list_linked_patients.html'
    context_object_name = 'list_linked_patients'
    model = AssociatedHealthProfessionalAndPatient
    paginate_by = 25

    # Get 25 queries of AssociatedHealthProfessionalAndPatient objects.
    def get_queryset(self):

        query_set = AssociatedHealthProfessionalAndPatient.objects.filter(associated_health_professional=self.request.user)

        return query_set
