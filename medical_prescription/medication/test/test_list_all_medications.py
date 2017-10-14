from django.test import TestCase
from medication.models import Medication
from medication.views import ListAllMedications
from user.models import HealthProfessional


class TestListAllMedications(TestCase):

    def setUp(self):

        # Making a HealthProfessional
        self.user = HealthProfessional()
        self.user.crm = "54321"
        self.user.save()

        self.view = ListAllMedications

        # Making medicati
        self.medication = Medication()
        self.medication.name = "Medicamento Teste"
        self.medication.active_ingredient = "Teste Lab"
        self.medication.health_professional = self.user
        self.medication.save()

        self.listing = Medication.objects.all()

    def test(self):
        instance = self.view()
        self.assertEqual(instance.get_queryset()[0], self.listing[0])
