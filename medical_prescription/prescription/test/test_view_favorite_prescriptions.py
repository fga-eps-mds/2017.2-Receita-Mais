from django.test import TestCase
from django.test.client import RequestFactory, Client

from disease.models import Disease
from medicine.models import ManipulatedMedicine
from user.models import Patient, HealthProfessional
from prescription.views import CreatePrescriptionView, ListFavoritePrescription


class TestListFavoritePrescription(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.view = CreatePrescriptionView()

        self.patient = Patient()
        self.patient.pk = 1
        self.patient.name = "Paciente de teste"
        self.patient.date_of_birth = "1991-10-21"
        self.patient.phone = "06199999999"
        self.patient.email = "paciente@emp.com"
        self.patient.sex = "M"
        self.patient.id_document = "1000331"
        self.patient.CEP = "72850735"
        self.patient.UF = "DF"
        self.patient.city = "Brasília"
        self.patient.neighborhood = "Asa sul"
        self.patient.complement = "Bloco 2 QD 701"
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

        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com',
                                                                          password='senha12')

    def teste_list_prescription(self):
        request = self.factory.get('/')
        request.user = self.health_professional

        response = ListFavoritePrescription.as_view()(request)
        self.assertEqual(response.status_code, 200)
