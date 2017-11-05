from django.test import TestCase
from medicine.models import Medicine
from medicine.views import ListAllMedicines
from user.models import HealthProfessional


class TestListAllMedicines(TestCase):

    def setUp(self):

        # Making a HealthProfessional

        self.view = ListAllMedicines

        # Making medicati
        self.medicine = Medicine()
        self.medicine.name = "Medicamento Teste"
        self.medicine.active_ingredient = "Teste Lab"
        self.medicine.save()

        self.listing = Medicine.objects.all()

    def test_medicine_is_show(self):
        instance = self.view()
        self.assertEqual(instance.get_queryset()[0], self.listing[0])
