from django.test import TestCase, RequestFactory
from medication.views import CreateMedicationView
from medication.forms import CreateMedicationForm
from user.models import HealthProfessional


class TesteCreateMedication(TestCase):

    def setUp(self):

        self.factory = RequestFactory()

        self.form_class = CreateMedicationForm
        self.class_name = CreateMedicationView

        # Creating a Health Professional
        self.health_professional = HealthProfessional()
        self.health_professionalcrm = '12345'
        self.health_professionalcrm_state = 'US'
        self.health_professional.save()

        self.invalid_name = 'a'*150
        self.valid_name = 'a'*150

    def test_redirect_false(self):
        my_class = self.class_name()
        self.assertNotEqual(my_class.get_success_url(), 'teste')

    def test_redirect_true(self):
        my_class = self.class_name()
        self.assertEqual(my_class.get_success_url(), '/pt-br/medication/list_medication/')
