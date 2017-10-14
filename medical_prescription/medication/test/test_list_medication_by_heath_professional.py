from django.test import TestCase, RequestFactory
from user.models import HealthProfessional
from medication.models import Medication
from medication.views import ListMedicationByHealthProfessional


class TestMedicationList(TestCase):

    def setUp(self):

        # Making a HealthProfessional
        self.user = HealthProfessional()
        self.user.crm = "54321"
        self.user.save()

        self.view = ListMedicationByHealthProfessional

        # Making medication
        self.medication = Medication()
        self.medication.name = "Medicamento Teste"
        self.medication.active_ingredient = "Teste Lab"
        self.medication.health_professional = self.user
        self.medication.save()

        self.factory = RequestFactory()

        self.health_professional_medications = Medication.objects.filter(health_professional=self.user)

    def teste_len_equal(self):
        self.assertEqual(len(self.health_professional_medications), 1)

    def teste_len_false(self):
        self.assertNotEqual(len(self.health_professional_medications), 50)

    def test_list(self):
            request = self.factory
            request.user = self.user
            list_medications = self.view.get_queryset(self.view)
            self.assertEqual(self.health_professional_medications, list_medications)
