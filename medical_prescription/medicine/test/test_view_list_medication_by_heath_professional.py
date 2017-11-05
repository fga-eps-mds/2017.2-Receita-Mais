from django.test import TestCase
from django.test.client import RequestFactory

from medicine.models import ManipulatedMedicine
from medicine.views import ListManipulatedMedicinenByHealthProfessional
from user.models import HealthProfessional


class TestManipulatedMedicineList(TestCase):

    def setUp(self):
        self.my_view = ListManipulatedMedicinenByHealthProfessional()
        self.factory = RequestFactory()

        # Making a HealthProfessional
        self.user = HealthProfessional()
        self.user.pk = 1
        self.user.email = "test@test.com"
        self.user.password = "test404"
        self.user.crm = "54321"
        self.user.save()

        self.medicine = ManipulatedMedicine()
        self.medicine.recipe_name = "Medicamento test"
        self.medicine.physical_form = "test forma fisica"
        self.medicine.quantity = 1.0
        self.medicine.measurement = "kg"
        self.medicine.composition = "teste"
        self.medicine.health_professional = self.user
        self.medicine.save()

        self.health_professional_medicines = ManipulatedMedicine.objects.filter(health_professional=self.user)

    def test_medicine_len_equal(self):
        self.assertEqual(len(self.health_professional_medicines), 1)

    def test_medicine_len_false(self):
        self.assertNotEqual(len(self.health_professional_medicines), 50)

    '''def test_get(self):
        self.client.login(email='test@test.com', password='test404')
        self.assertTrue('list_medications' in self.resp.context)'''
