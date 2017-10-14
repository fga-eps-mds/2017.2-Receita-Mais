from django.test import TestCase

from medication.forms import CreateMedicationForm
from user.models import HealthProfessional
from medication.models import Medication


class TestFormMedication(TestCase):
    def setUp(self):
        self.health_professional = HealthProfessional()
        self.health_professional_crm = '12345'
        self.health_professional_crm_state = 'AM'
        self.health_professional.save()

        self.medication = Medication()
        self.medication.name = "Medicamento Teste"
        self.medication.active_ingredient = "Teste Lab"
        self.medication.laboratory = "Test Lab"
        self.medication.description = "This is a Description"
        self.medication.health_professional = self.health_professional
        self.medication.is_restricted = False
        self.medication.save()

        self.empty_string = ""

    def test_medication_form_is_valid(self):
        form_data = {
            'name': self.medication.name,
            'active_ingredient': self.medication.active_ingredient,
            'laboratory': self.medication.laboratory,
            'description': self.medication.description,
            'is_restricted': self.medication.is_restricted,
            'health_professional': self.health_professional
        }
        form = CreateMedicationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_medication_form_name_invalid(self):
        form_data = {
            'name': self.empty_string,
            'active_ingredient': self.medication.active_ingredient,
            'laboratory': self.medication.laboratory,
            'description': self.medication.description,
            'is_restricted': self.medication.is_restricted,
            'health_professional': self.health_professional
        }
        form = CreateMedicationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_medication_form_active_ingredient_invalid(self):
        form_data = {
            'name': self.medication.name,
            'active_ingredient': self.empty_string,
            'laboratory': self.medication.laboratory,
            'description': self.medication.description,
            'is_restricted': self.medication.is_restricted,
            'health_professional': self.health_professional
        }
        form = CreateMedicationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_medication_form_laboratory_invalid(self):
        form_data = {
            'name': self.medication.name,
            'active_ingredient': self.medication.active_ingredient,
            'laboratory': self.empty_string,
            'description': self.medication.description,
            'is_restricted': self.medication.is_restricted,
            'health_professional': self.health_professional
        }
        form = CreateMedicationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_medication_form_description_invalid(self):
        form_data = {
            'name': self.medication.name,
            'active_ingredient': self.medication.active_ingredient,
            'laboratory': self.medication.laboratory,
            'description': self.empty_string,
            'is_restricted': self.medication.is_restricted,
            'health_professional': self.health_professional
        }
        form = CreateMedicationForm(data=form_data)
        self.assertFalse(form.is_valid())
