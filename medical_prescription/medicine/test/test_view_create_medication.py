from django.test import TestCase, RequestFactory
from medicine.views import CreateMedicineView
from medicine.forms import CreateManipulatedMedicineForm
from user.models import HealthProfessional


class TesteCreateMedicine(TestCase):

    def setUp(self):

        self.factory = RequestFactory()

        self.form_class = CreateManipulatedMedicineForm
        self.class_name = CreateMedicineView

        # Creating a Health Professional
        self.health_professional = HealthProfessional()
        self.health_professionalcrm = '12345'
        self.health_professionalcrm_state = 'US'
        self.health_professional.save()

        self.invalid_name = 'a'*150
        self.valid_name = 'a'*150

    def test_medicine_redirect_false(self):
        my_class = self.class_name()
        self.assertNotEqual(my_class.get_success_url(), 'teste')

    def test_medicine_redirect_true(self):
        my_class = self.class_name()
        self.assertEqual(my_class.get_success_url(), '/pt-br/medicine/list_all_medicines/')
