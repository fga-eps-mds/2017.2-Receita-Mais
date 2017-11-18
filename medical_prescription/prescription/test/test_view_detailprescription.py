# Django
from django.test import TestCase
from django.test.client import RequestFactory

# Django Local
from medicine.models import (Medicine,
                             ManipulatedMedicine,
                             )
from prescription.models import (NoPatientPrescription,
                                 PrescriptionHasManipulatedMedicine,
                                 PrescriptionHasMedicine,
                                 )
from user.models import (HealthProfessional)
from prescription import constants
from prescription.views import ShowDetailPrescriptionView


class TestShowDetailPrescriptionView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com',
                                                                          password='senha12')

        self.manipulated_medicine = ManipulatedMedicine()
        self.manipulated_medicine.pk = 1
        self.manipulated_medicine.recipe_name = "teste"
        self.manipulated_medicine.physical_form = "asdadsafdf"
        self.manipulated_medicine.quantity = 12
        self.manipulated_medicine.measurement = "kg"
        self.manipulated_medicine.composition = "aosdjoaisjdoiajsdoij"
        self.manipulated_medicine.health_professional = self.health_professional
        self.manipulated_medicine.save()

        self.medicine = Medicine()
        self.medicine.name = "Medicamento Teste"
        self.medicine.active_ingredient = "Teste Lab"
        self.medicine.save()

        self.posology = "Medicamento de Teste"
        self.quantity = 1
        self.via = constants.VIA_CHOICES[0][0]

        self.patient = "Carlos Nogueira"

        self.prescription = NoPatientPrescription()
        self.prescription.patient = self.patient
        self.prescription.cid = None
        self.prescription.health_professional = self.health_professional
        self.prescription.pk = 1
        self.prescription.save()

        self.has_manipulated_medicine = PrescriptionHasMedicine()
        self.has_manipulated_medicine.prescription_medicine = self.prescription
        self.has_manipulated_medicine.medicine = self.medicine
        self.has_manipulated_medicine.posology = self.posology
        self.has_manipulated_medicine.via = self.via
        self.has_manipulated_medicine.quantity = self.quantity
        self.has_manipulated_medicine.save()

        self.has_medicine = PrescriptionHasManipulatedMedicine()
        self.has_medicine.prescription_medicine = self.prescription
        self.has_medicine.manipulated_medicine = self.manipulated_medicine
        self.has_medicine.posology = self.posology
        self.has_medicine.via = self.via
        self.has_medicine.quantity = self.quantity
        self.has_medicine.save()

    def test_prescription_get_with_health_professional(self):
        request = self.factory.get('/prescription/show_prescription/1')
        request.user = self.health_professional

        # Get the response
        response = ShowDetailPrescriptionView.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)
