from django.test import TestCase
from django.test.client import RequestFactory, Client

from prescription.models import (
                                NoPatientPrescription,
                                PatientPrescription,
                                PrescriptionHasManipulatedMedicine,
                                PrescriptionNewRecommendation,
                                PrescriptionHasMedicine,
                                PrescriptionDefaultExam,
                                PrescriptionCustomExam,
                                Pattern,
                                )
from disease.models import Disease
from exam.models import DefaultExam, CustomExam
from medicine.models import Medicine, ManipulatedMedicine
from user.models import Patient, HealthProfessional
from prescription.views import PrintPrescription
from recommendation.models import NewRecommendation


class TestPrintPrescription(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.view = PrintPrescription.generate_pdf

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
        self.health_professional.specialty_first = 'Nutricao'
        self.health_professional.specialty_second = 'Pediatria'
        self.health_professional.save()

        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com',
                                                                          password='senha12')

        self.disease = Disease()
        self.disease.pk = 1
        self.disease.id_cid_10 = "A01"
        self.disease.description = "A random disease"
        self.disease.save()

        self.prescription = NoPatientPrescription()
        self.prescription.pk = 1
        self.prescription.health_professional = self.health_professional
        self.prescription.cid = self.disease
        self.prescription.patient = "Algum nome"
        self.prescription.save()

        self.prescription_2 = NoPatientPrescription()
        self.prescription_2.pk = 2
        self.prescription_2.health_professional = self.health_professional
        self.prescription_2.cid = self.disease
        self.prescription_2.patient = "Algum nome"
        self.prescription_2.save()

        self.prescription_3 = PatientPrescription()
        self.prescription_3.pk = 3
        self.prescription_3.health_professional = self.health_professional
        self.prescription_3.cid = self.disease
        self.prescription_3.patient = self.patient
        self.prescription_3.save()

        self.prescription_4 = PatientPrescription()
        self.prescription_4.pk = 4
        self.prescription_4.health_professional = self.health_professional
        self.prescription_4.cid = self.disease
        self.prescription_4.patient = self.patient
        self.prescription_4.save()

        self.prescription_5 = PatientPrescription()
        self.prescription_5.pk = 5
        self.prescription_5.health_professional = self.health_professional
        self.prescription_5.cid = self.disease
        self.prescription_5.patient = self.patient
        self.prescription_5.save()

        self.manipulated_medicine = ManipulatedMedicine()
        self.manipulated_medicine.pk = 1
        self.manipulated_medicine.recipe_name = "teste"
        self.manipulated_medicine.physical_form = "asdadsafdf"
        self.manipulated_medicine.quantity = 12
        self.manipulated_medicine.measurement = "kg"
        self.manipulated_medicine.composition = "aosdjoaisjdoiajsdoij"
        self.manipulated_medicine.health_professional = self.health_professional
        self.manipulated_medicine.save()

        self.manipulated_medicine_2 = ManipulatedMedicine()
        self.manipulated_medicine_2.pk = 2
        self.manipulated_medicine_2.recipe_name = "teste"
        self.manipulated_medicine_2.physical_form = "asdadsafdf"
        self.manipulated_medicine_2.quantity = 12
        self.manipulated_medicine_2.measurement = "kg"
        self.manipulated_medicine_2.composition = "aosdjoaisjdoiajsdoij"
        self.manipulated_medicine_2.health_professional = self.health_professional
        self.manipulated_medicine_2.save()

        self.hasmanipulated_medicine = PrescriptionHasManipulatedMedicine()
        self.hasmanipulated_medicine.manipulated_medicine = self.manipulated_medicine
        self.hasmanipulated_medicine.posology = "asd"
        self.hasmanipulated_medicine.quantity = 1
        self.hasmanipulated_medicine.pk = 2
        self.hasmanipulated_medicine.via = 'Via Intravenosa'
        self.hasmanipulated_medicine.prescription_medicine = self.prescription
        self.hasmanipulated_medicine.save()

        self.hasmanipulated_medicine = PrescriptionHasManipulatedMedicine()
        self.hasmanipulated_medicine.manipulated_medicine = self.manipulated_medicine_2
        self.hasmanipulated_medicine.posology = "asd"
        self.hasmanipulated_medicine.quantity = 1
        self.hasmanipulated_medicine.pk = 12
        self.hasmanipulated_medicine.via = 'Via Intravenosa'
        self.hasmanipulated_medicine.prescription_medicine = self.prescription
        self.hasmanipulated_medicine.save()

        self.hasmanipulated_medicine = PrescriptionHasManipulatedMedicine()
        self.hasmanipulated_medicine.manipulated_medicine = self.manipulated_medicine
        self.hasmanipulated_medicine.posology = "asd"
        self.hasmanipulated_medicine.quantity = 1
        self.hasmanipulated_medicine.pk = 4
        self.hasmanipulated_medicine.via = 'Via Intravenosa'
        self.hasmanipulated_medicine.prescription_medicine = self.prescription_2
        self.hasmanipulated_medicine.save()

        self.recommendation = NewRecommendation()
        self.recommendation.recommendation_description = "recomendacao de teste"
        self.recommendation.save()

        self.prescription_has_recommendation = PrescriptionNewRecommendation()
        self.prescription_has_recommendation.prescription = self.prescription
        self.prescription_has_recommendation.recommendation = self.recommendation
        self.prescription_has_recommendation.save()

        self.prescription_has_recommendation = PrescriptionNewRecommendation()
        self.prescription_has_recommendation.prescription = self.prescription_3
        self.prescription_has_recommendation.recommendation = self.recommendation
        self.prescription_has_recommendation.save()

        self.medicine = Medicine()
        self.medicine.name = "asdoajsdoiasj"
        self.medicine.active_ingredient = "dsofaksdofk"
        self.medicine.laboratory = "dofijasoifjjf"
        self.medicine.description = "oiajdoaisjddj"
        self.medicine.save()

        self.medicine_2 = Medicine()
        self.medicine_2.name = "asdoajsdoiasj"
        self.medicine_2.active_ingredient = "dsofaksdofk"
        self.medicine_2.laboratory = "dofijasoifjjf"
        self.medicine_2.description = "oiajdoaisjddj"
        self.medicine_2.save()

        self.prescription_has_medicine = PrescriptionHasMedicine()
        self.prescription_has_medicine.medicine = self.medicine
        self.prescription_has_medicine.posology = "asd"
        self.prescription_has_medicine.quantity = 1
        self.prescription_has_medicine.pk = 2
        self.prescription_has_medicine.via = 'Via Intravenosa'
        self.prescription_has_medicine.prescription_medicine = self.prescription
        self.prescription_has_medicine.save()

        self.prescription_has_medicine = PrescriptionHasMedicine()
        self.prescription_has_medicine.medicine = self.medicine_2
        self.prescription_has_medicine.posology = "asd"
        self.prescription_has_medicine.quantity = 1
        self.prescription_has_medicine.pk = 21
        self.prescription_has_medicine.via = 'Via Intravenosa'
        self.prescription_has_medicine.prescription_medicine = self.prescription
        self.prescription_has_medicine.save()

        self.default_exam = DefaultExam()
        self.default_exam.id_tuss = 'oiafj'
        self.default_exam.save()

        self.custom_exam = CustomExam()
        self.custom_exam.health_professional_FK = self.health_professional
        self.custom_exam.save()

        self.prescription_default_exam = PrescriptionDefaultExam()
        self.prescription_default_exam.exam = self.default_exam
        self.prescription_default_exam.prescription = self.prescription
        self.prescription_default_exam.save()

        self.prescription_default_exam = PrescriptionDefaultExam()
        self.prescription_default_exam.exam = self.default_exam
        self.prescription_default_exam.prescription = self.prescription_4
        self.prescription_default_exam.save()

        self.prescription_custom_exam = PrescriptionCustomExam()
        self.prescription_custom_exam.exam = self.custom_exam
        self.prescription_custom_exam.prescription = self.prescription
        self.prescription_custom_exam.save()

        self.pattern = Pattern()
        self.pattern.name = "Pattern de teste"
        self.pattern.user_creator = self.health_professional
        self.pattern.clinic = "clinica de teste"
        self.pattern.header = "header de teste"
        self.pattern.font = 'Helvetica'
        self.pattern.font_size = '12'
        self.pattern.footer = "footer de teste"
        self.pattern.pagesize = "letter"
        self.pattern.pk = 1
        self.pattern.logo = None
        self.pattern.save()

        self.pattern = Pattern()
        self.pattern.name = "Pattern de teste"
        self.pattern.user_creator = self.health_professional
        self.pattern.clinic = "clinica de teste"
        self.pattern.header = "header de teste"
        self.pattern.font = 'Helvetica'
        self.pattern.font_size = '12'
        self.pattern.footer = "footer de teste"
        self.pattern.pagesize = "A4"
        self.pattern.pk = 2
        self.pattern.logo = None
        self.pattern.save()

        self.pattern = Pattern()
        self.pattern.name = "Pattern de teste"
        self.pattern.user_creator = self.health_professional
        self.pattern.clinic = "clinica de teste"
        self.pattern.header = "header de teste"
        self.pattern.font = 'Helvetica'
        self.pattern.font_size = '12'
        self.pattern.footer = "footer de teste"
        self.pattern.pagesize = "A5"
        self.pattern.pk = 3
        self.pattern.logo = None
        self.pattern.save()

    def test_print_prescription_get_letter(self):
        request = self.factory.get('/prescription/print_prescription/1/3')
        response = self.view(request, pk=1, jk=1)
        self.assertEqual(response.status_code, 200)

    def test_print_prescription_get_A4(self):
        request = self.factory.get('/prescription/print_prescription/1/3')
        response = self.view(request, pk=1, jk=2)
        self.assertEqual(response.status_code, 200)

    def test_print_prescription_get_A5(self):
        request = self.factory.get('/prescription/print_prescription/1/3')
        response = self.view(request, pk=1, jk=3)
        self.assertEqual(response.status_code, 200)

    def test_print_prescription_get_invalid_medicine(self):
        request = self.factory.get('/prescription/print_prescription/2/3')
        response = self.view(request, pk=2, jk=3)
        self.assertEqual(response.status_code, 200)

    def test_print_prescription_get_invalid_recommendation(self):
        request = self.factory.get('/prescription/print_prescription/3/3')
        response = self.view(request, pk=3, jk=3)
        self.assertEqual(response.status_code, 200)

    def test_print_prescription_get_invalid_exam(self):
        request = self.factory.get('/prescription/print_prescription/4/3')
        response = self.view(request, pk=4, jk=3)
        self.assertEqual(response.status_code, 200)

    def test_print_prescription_get_invalid(self):
        request = self.factory.get('/prescription/print_prescription/5/3')
        response = self.view(request, pk=5, jk=3)
        self.assertEqual(response.status_code, 200)

    def test_print_prescription_get_invalid(self):
        request = self.factory.get('/prescription/print_prescription/5/3')
        response = self.view(request, pk=3, jk=1)
        self.assertEqual(response.status_code, 200)
