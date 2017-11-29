from django.test import TestCase
from django.test.client import RequestFactory, Client

from prescription.models import Pattern
from user.models import Patient, HealthProfessional
from prescription.views import ListPatterns, CreatePatternView


class TestListPatterns(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.view = CreatePatternView()

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

        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com',
                                                                  password='senha12')

        self.pattern = Pattern()
        self.pattern.name = "Nome teste"
        self.pattern.user_creator = self.health_professional
        self.pattern.font = "Times-Roman"
        self.pattern.font_size = "12"
        self.pattern.pagesize = "letter"
        self.pattern.clinic = "Clinic name"
        self.pattern.header = "Header"
        self.pattern.footer = "Footer"

    def teste_list_prescription(self):
        request = self.factory.get('prescription/list_patterns/')
        request.user = self.health_professional

        response = ListPatterns.as_view()(request)
        self.assertEqual(response.status_code, 200)
