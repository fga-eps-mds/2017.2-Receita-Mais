# standard library
import json
import logging

# django
from django.test import TestCase
from django.test.client import RequestFactory
from django.http import HttpResponse
from django.test.client import Client

# local djngo.
from prescription.views import SuggestionsCid
# Django Local
from disease.models import Disease
from medicine.models import (ManipulatedMedicine,
                             Medicine,
                             )
from user.models import Patient, HealthProfessional
from prescription.views import CreateCopyPrescription
from prescription.models import (NoPatientPrescription,
                                 PatientPrescription,
                                 PrescriptionHasManipulatedMedicine,
                                 PrescriptionHasMedicine,
                                 PrescriptionDefaultExam,
                                 PrescriptionNewRecommendation,
                                 PrescriptionCustomExam,
                                 )
from prescription import constants
from recommendation.models import NewRecommendation
from exam.models import (DefaultExam,
                         CustomExam,
                         )
from user.constants import DEFAULT_LOGGER

# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(DEFAULT_LOGGER)


class TestRequiredSuggestionCid(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.view = CreateCopyPrescription()

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

        self.medicine = Medicine()
        self.medicine.name = "Medicamento Teste"
        self.medicine.active_ingredient = "Teste Lab"
        self.medicine.save()

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

        self.health_professional_2 = HealthProfessional.objects.create_user(email='doctor@doctor.com',
                                                                            password='senha12')

        self.nopatientprescription = NoPatientPrescription()
        self.nopatientprescription.patient = self.patient
        self.nopatientprescription.cid = self.disease
        self.nopatientprescription.health_professional = self.health_professional_2
        self.nopatientprescription.patient = "Junior Marques"
        self.nopatientprescription.save()

        self.patientprescription = PatientPrescription()
        self.patientprescription.patient = self.patient
        self.patientprescription.cid = self.disease
        self.patientprescription.health_professional = self.health_professional_2
        self.patientprescription.patient = self.patient
        self.patientprescription.save()

        self.posology = "Medicamento de Teste"
        self.quantity = 1
        self.via = constants.VIA_CHOICES[0][0]

        self.has_medicine = PrescriptionHasMedicine()
        self.has_medicine.prescription_medicine = self.nopatientprescription.prescription_ptr
        self.has_medicine.medicine = self.medicine
        self.has_medicine.posology = self.posology
        self.has_medicine.via = self.via
        self.has_medicine.quantity = self.quantity
        self.has_medicine.save()

        self.has_manipulated = PrescriptionHasManipulatedMedicine()
        self.has_manipulated.prescription_medicine = self.nopatientprescription.prescription_ptr
        self.has_manipulated.manipulated_medicine = self.manipulated_medicine
        self.has_manipulated.posology = self.posology
        self.has_manipulated.via = self.via
        self.has_manipulated.quantity = self.quantity
        self.has_manipulated.save()

        self.manipulated_medicine = ManipulatedMedicine()
        self.manipulated_medicine.pk = 1
        self.manipulated_medicine.recipe_name = "teste"
        self.manipulated_medicine.physical_form = "asdadsafdf"
        self.manipulated_medicine.quantity = 12
        self.manipulated_medicine.measurement = "kg"
        self.manipulated_medicine.composition = "aosdjoaisjdoiajsdoij"
        self.manipulated_medicine.health_professional = self.health_professional
        self.manipulated_medicine.save()

        self.hasmanipulated_medicine = PrescriptionHasManipulatedMedicine()
        self.hasmanipulated_medicine.manipulated_medicine = self.manipulated_medicine
        self.hasmanipulated_medicine.posology = "asd"
        self.hasmanipulated_medicine.quantity = 1
        self.hasmanipulated_medicine.pk = 2
        self.hasmanipulated_medicine.via = 'Via Intravenosa'
        self.hasmanipulated_medicine.prescription_medicine = self.nopatientprescription.prescription_ptr
        self.hasmanipulated_medicine.save()

        self.hasmanipulated_medicine = PrescriptionHasManipulatedMedicine()
        self.hasmanipulated_medicine.manipulated_medicine = self.manipulated_medicine
        self.hasmanipulated_medicine.posology = "asd"
        self.hasmanipulated_medicine.quantity = 1
        self.hasmanipulated_medicine.pk = 12
        self.hasmanipulated_medicine.via = 'Via Intravenosa'
        self.hasmanipulated_medicine.prescription_medicine = self.nopatientprescription.prescription_ptr
        self.hasmanipulated_medicine.save()

        self.recommendation = NewRecommendation()
        self.recommendation.recommendation_description = "recomendacao de teste"
        self.recommendation.save()

        self.prescription_has_recommendation = PrescriptionNewRecommendation()
        self.prescription_has_recommendation.prescription = self.nopatientprescription.prescription_ptr
        self.prescription_has_recommendation.recommendation = self.recommendation
        self.prescription_has_recommendation.save()

        self.prescription_has_recommendation = PrescriptionNewRecommendation()
        self.prescription_has_recommendation.prescription = self.nopatientprescription.prescription_ptr
        self.prescription_has_recommendation.recommendation = self.recommendation
        self.prescription_has_recommendation.save()

        self.medicine = Medicine()
        self.medicine.name = "asdoajsdoiasj"
        self.medicine.active_ingredient = "dsofaksdofk"
        self.medicine.laboratory = "dofijasoifjjf"
        self.medicine.description = "oiajdoaisjddj"
        self.medicine.save()

        self.prescription_has_medicine = PrescriptionHasMedicine()
        self.prescription_has_medicine.medicine = self.medicine
        self.prescription_has_medicine.posology = "asd"
        self.prescription_has_medicine.quantity = 1
        self.prescription_has_medicine.pk = 2
        self.prescription_has_medicine.via = 'Via Intravenosa'
        self.prescription_has_medicine.prescription_medicine = self.nopatientprescription.prescription_ptr
        self.prescription_has_medicine.save()

        self.default_exam = DefaultExam()
        self.default_exam.id_tuss = 'oiafj'
        self.default_exam.save()

        self.custom_exam = CustomExam()
        self.custom_exam.health_professional_FK = self.health_professional
        self.custom_exam.save()

        self.prescription_default_exam = PrescriptionDefaultExam()
        self.prescription_default_exam.exam = self.default_exam
        self.prescription_default_exam.prescription = self.nopatientprescription.prescription_ptr
        self.prescription_default_exam.save()

        self.prescription_custom_exam = PrescriptionCustomExam()
        self.prescription_custom_exam.exam = self.custom_exam
        self.prescription_custom_exam.prescription = self.nopatientprescription.prescription_ptr
        self.prescription_custom_exam.save()

    def test_prescription_request_no_disease(self):
        request = self.factory.post(
            '/ajax/suggestions_cid/',
            {'id': self.disease.pk},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
            )
        request.user = self.health_professional_2
        response = SuggestionsCid.as_view()(request)
        print(response)
        self.assertEquals(response.status_code, 200)

    def test_prescription_request_autocomplete_cid_return_one_disease(self):
        request = self.factory.post('/ajax/suggestions_cid/', {'id': self.disease.pk})
        request.user = self.health_professional
        response = SuggestionsCid.as_view()(request)
        self.assertNotEquals(response, HttpResponse)
