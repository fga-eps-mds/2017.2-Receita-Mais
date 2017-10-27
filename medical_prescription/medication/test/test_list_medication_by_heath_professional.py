from django.test import TestCase
from django.test.client import RequestFactory

from user.models import HealthProfessional
from medication.models import Medication
from medication.views import ListMedicationByHealthProfessional


class TestMedicationList(TestCase):

    def setUp(self):
        self.my_view = ListMedicationByHealthProfessional()
        self.factory = RequestFactory()

        # Making a HealthProfessional
        self.user = HealthProfessional()
        self.user.pk = 1
        self.user.email = "test@test.com"
        self.user.password = "test404"
        self.user.crm = "54321"
        self.user.save()

        self.medication = Medication()
        self.medication.name = "Medicamento Teste"
        self.medication.active_ingredient = "Teste Lab"
        self.medication.health_professional = self.user
        self.medication.save()

        self.health_professional_medications = Medication.objects.filter(health_professional=self.user)

    def teste_len_equal(self):
        self.assertEqual(len(self.health_professional_medications), 1)

    def teste_len_false(self):
        self.assertNotEqual(len(self.health_professional_medications), 50)
