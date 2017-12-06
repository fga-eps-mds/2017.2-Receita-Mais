from django.test import TestCase
from django.test.client import RequestFactory, Client
from unittest.mock import patch, MagicMock

from disease.models import Disease
from medicine.models import ManipulatedMedicine
from user.models import (Patient,
                         HealthProfessional,
                         AssociatedHealthProfessionalAndPatient,
                         SendInvitationProfile)
from prescription.views import CreatePrescriptionView
from prescription.models import NoPatientPrescription, PatientPrescription


class TestCreatePrescription(TestCase):
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
        self.patient.is_active = True
        self.patient.save()

        self.health_professional = HealthProfessional()
        self.health_professional.pk = 1
        self.health_professional.crm = '12345'
        self.health_professional.crm_state = 'US'
        self.health_professional.is_active = True
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

        self.relation = AssociatedHealthProfessionalAndPatient()
        self.relation.associated_health_professional = self.health_professional
        self.relation.associated_patient = self.patient
        self.relation.is_active = True
        self.relation.save()

        self.not_patient = Patient()
        self.not_patient.email = "teste@patient.com"
        self.not_patient.is_active = True
        self.not_patient.save()

        self.patient_not_actived = Patient()
        self.patient_not_actived.email = "not@pac.com"
        self.patient_not_actived.is_active = False
        self.patient_not_actived.save()

        self.invitation = SendInvitationProfile()
        self.invitation.patient = self.patient_not_actived
        self.invitation.save()

    def test_prescription_get(self):
        request = self.factory.get('/prescription/create_modal/')
        response = self.view.get(request)
        self.assertEqual(response.status_code, 200)

    @patch('prescription.models.NoPatientPrescription.save', MagicMock(name="save"))
    @patch('prescription.models.PrescriptionNewRecommendation.save', MagicMock(name="save"))
    def test_prescription_post_with_health_professional(self):
        context = {'form_medicine-TOTAL_FORMS': 1,
                   'form_medicine-INITIAL_FORMS': 0,
                   'form_recommendation-TOTAL_FORMS': 1,
                   'form_recommendation-INITIAL_FORMS': 0,
                   'form_exam-TOTAL_FORMS': 1,
                   'form_exam-INITIAL_FORMS': 0,
                   'patient': "JOAO",
                   'patient_id': 0,
                   'cid_id': 1,
                   'medicine_type': 'manipulated_medicine',
                   'medicine_id': 1,
                   'quantity': 10,
                   'posology': 'nao fazer nada',
                   'via': 'Via oral',
                   }

        request = self.factory.post('/prescription/create_modal/', context)
        request.user = self.health_professional

        # Get the response
        response = CreatePrescriptionView.as_view()(request)
        self.assertEqual(response.status_code, 200)

        # # Check save was called
        self.assertTrue(NoPatientPrescription.save.called)
        self.assertEqual(NoPatientPrescription.save.call_count, 1)

    @patch('prescription.models.PatientPrescription.save', MagicMock(name="save"))
    @patch('prescription.models.PrescriptionNewRecommendation.save', MagicMock(name="save"))
    def test_prescription_post_with_health_professional_patient(self):
        context = {'form_medicine-TOTAL_FORMS': 1,
                   'form_medicine-INITIAL_FORMS': 0,
                   'form_recommendation-TOTAL_FORMS': 1,
                   'form_recommendation-INITIAL_FORMS': 0,
                   'form_exam-TOTAL_FORMS': 1,
                   'form_exam-INITIAL_FORMS': 0,
                   'patient': "JOAO",
                   'patient_id': 1,
                   'email': self.patient.email,
                   'cid_id': 1,
                   'medicine_type': 'manipulated_medicine',
                   'medicine_id': 1,
                   'quantity': 10,
                   'posology': 'nao fazer nada',
                   'via': 'Via oral',
                   }

        request = self.factory.post('/prescription/create_modal/', context)
        request.user = self.health_professional

        # Get the response
        response = CreatePrescriptionView.as_view()(request)
        self.assertEqual(response.status_code, 200)

        # # Check save was called
        self.assertTrue(PatientPrescription.save.called)
        self.assertEqual(PatientPrescription.save.call_count, 1)

    @patch('prescription.models.PatientPrescription.save', MagicMock(name="save"))
    @patch('prescription.models.PrescriptionNewRecommendation.save', MagicMock(name="save"))
    def test_prescription_post_with_patient_not_linked(self):
        context = {'form_medicine-TOTAL_FORMS': 1,
                   'form_medicine-INITIAL_FORMS': 0,
                   'form_recommendation-TOTAL_FORMS': 1,
                   'form_recommendation-INITIAL_FORMS': 0,
                   'form_exam-TOTAL_FORMS': 1,
                   'form_exam-INITIAL_FORMS': 0,
                   'patient': "JOAO",
                   'email': self.not_patient.email,
                   'cid_id': 1,
                   'medicine_type': 'manipulated_medicine',
                   'medicine_id': 1,
                   'quantity': 10,
                   'posology': 'nao fazer nada',
                   'via': 'Via oral',
                   }

        request = self.factory.post('/prescription/create_modal/', context)
        request.user = self.health_professional

        # Get the response
        response = CreatePrescriptionView.as_view()(request)
        self.assertEqual(response.status_code, 200)

        # Checking the creation of link between users.
        link = AssociatedHealthProfessionalAndPatient.objects.filter(associated_health_professional=self.health_professional,
                                                                     associated_patient=self.not_patient)
        self.assertTrue(link.exists())
        self.assertTrue(link.first().is_active)

        # # Check save was called
        self.assertTrue(PatientPrescription.save.called)
        self.assertEqual(PatientPrescription.save.call_count, 1)

    @patch('prescription.models.PatientPrescription.save', MagicMock(name="save"))
    @patch('prescription.models.PrescriptionNewRecommendation.save', MagicMock(name="save"))
    def test_prescription_post_with_patient_doesnt_exist(self):
        context = {'form_medicine-TOTAL_FORMS': 1,
                   'form_medicine-INITIAL_FORMS': 0,
                   'form_recommendation-TOTAL_FORMS': 1,
                   'form_recommendation-INITIAL_FORMS': 0,
                   'form_exam-TOTAL_FORMS': 1,
                   'form_exam-INITIAL_FORMS': 0,
                   'patient': "JOAO",
                   'email': "patient@doesnt.com",
                   'cid_id': 1,
                   'medicine_type': 'manipulated_medicine',
                   'medicine_id': 1,
                   'quantity': 10,
                   'posology': 'nao fazer nada',
                   'via': 'Via oral',
                   }

        request = self.factory.post('/prescription/create_modal/', context)
        request.user = self.health_professional

        # Get the response
        response = CreatePrescriptionView.as_view()(request)
        self.assertEqual(response.status_code, 200)

        # Checking the creation of patient not existence.
        patient = Patient.objects.filter(email="patient@doesnt.com")
        self.assertTrue(patient.exists())

        # Checking the creation of link between users.
        link = AssociatedHealthProfessionalAndPatient.objects.filter(associated_health_professional=self.health_professional,
                                                                     associated_patient=patient.first())
        self.assertTrue(link.exists())
        self.assertFalse(link.first().is_active)

        # Check save was called
        self.assertTrue(PatientPrescription.save.called)
        self.assertEqual(PatientPrescription.save.call_count, 1)

    @patch('prescription.models.PatientPrescription.save', MagicMock(name="save"))
    @patch('prescription.models.PrescriptionNewRecommendation.save', MagicMock(name="save"))
    def test_prescription_post_with_patient_not_actived(self):
        context = {'form_medicine-TOTAL_FORMS': 1,
                   'form_medicine-INITIAL_FORMS': 0,
                   'form_recommendation-TOTAL_FORMS': 1,
                   'form_recommendation-INITIAL_FORMS': 0,
                   'form_exam-TOTAL_FORMS': 1,
                   'form_exam-INITIAL_FORMS': 0,
                   'patient': "JOAO",
                   'email': self.patient_not_actived.email,
                   'cid_id': 1,
                   'medicine_type': 'manipulated_medicine',
                   'medicine_id': 1,
                   'quantity': 10,
                   'posology': 'nao fazer nada',
                   'via': 'Via oral',
                   }

        request = self.factory.post('/prescription/create_modal/', context)
        request.user = self.health_professional

        # Get the response
        response = CreatePrescriptionView.as_view()(request)
        self.assertEqual(response.status_code, 200)

        # # Check save was called
        self.assertTrue(PatientPrescription.save.called)
        self.assertEqual(PatientPrescription.save.call_count, 1)

    def test_prescription_get_with_health_professional(self):

        request = self.factory.post('/prescription/create_modal/')
        request.user = self.health_professional

        # Get the response
        response = CreatePrescriptionView.as_view()(request)
        self.assertEqual(response.status_code, 200)
