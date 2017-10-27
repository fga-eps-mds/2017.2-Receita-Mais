from django.db import IntegrityError
from django.test import TestCase
from django.test.client import RequestFactory, Client

from disease.models import Disease
from medicine.models import ManipulatedMedicine
from user.models import Patient, HealthProfessional
from prescription.forms import MedicinePrescriptionForm
from prescription.views import CreatePrescriptionMedicine


class TestCreatePrescriptionMedicine(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.view = CreatePrescriptionMedicine()

        self.patient = Patient()
        self.patient.pk = 1
        self.patient.name = "Paciente de teste"
        self.patient.date_of_birth = "1991-10-21"
        self.patient.phone = "06199999999"
        self.patient.email = "paciente@emp.com"
        self.patient.sex = "M"
        self.patient.id_document = "1000331"
        self.patient.save()

        self.health_professional = HealthProfessional()
        self.health_professional.pk = 1
        self.health_professional.crm = '12345'
        self.health_professional.crm_state = 'US'
        self.health_professional.save()

        self.manipulated_medicine = ManipulatedMedicine()
        self.manipulated_medicine.pk = 1
        self.manipulated_medicine.recipe_name = "teste"
        self.manipulated_medicine.physical_form = "asdadsafdf"
        self.manipulated_medicine.quantity = 12
        self.manipulated_medicine.measurement = "kg"
        self.manipulated_medicine.composition = "aosdjoaisjdoiajsdoij"
        self.manipulated_medicine.health_professional = self.health_professional
        self.manipulated_medicine.save()

        self.disease = Disease()
        self.disease.pk = 1
        self.disease.id_cid_10 = "A01"
        self.disease.description = "A random disease"
        self.disease.save()    

    def test_get(self):
        request = self.factory.get('/prescription/create_modal/')
        response = self.view.get(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        context = {'form-TOTAL_FORMS': 1, 
                   'form-INITIAL_FORMS': 0,
                   'patient_id': 1,
                   'cid_id': 1,
                   'medicine_type': 'manipulated_medicine',
                   'medicine_id': 1,
                   'quantity': 10,
                   'posology': 'nao fazer nada'
                   }
        response = self.client.post('/prescription/create_modal/', context)

        self.assertEqual(response.status_code, 200)

    def test_invalid_form(self):
        context = {'form-TOTAL_FORMS': 1, 
                   'form-INITIAL_FORMS': 0,
                   'patient_id': 1,
                   'cid_id': 15,
                   'medicine_type': 'manipulated_medicine',
                   'medicine_id': 1,
                   'quantity': 10,
                   'posology': 'nao fazer nada'
                   }

        form = MedicinePrescriptionForm(context)

        self.assertFalse(form.is_valid())
