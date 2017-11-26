from django.test import TestCase
from django.test.client import RequestFactory, Client

from prescription.models import Pattern
from prescription.views import CreatePatternView
from user.models import HealthProfessional


class TestCreatePattern(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.my_class = Pattern
        self.my_view = CreatePatternView()

        self.user = HealthProfessional()
        self.user.email = 'email@email.com'
        self.user.save()

        self.name = "Pattern de teste"
        self.user_creator = self.user
        self.clinic = "clinica de teste"
        self.header = "header de teste"
        self.font = 'Helvetica'
        self.font_size = '12'
        self.footer = "footer de teste"
        self.pagesize = "letter"

    def test_pattern_redirect_valid(self):
        data = {
                'name': self.name,
                'clinic': self.clinic,
                'font': 'Helvetica',
                'font_size': '12',
                'header': self.header,
                'footer': self.footer,
                'pagesize': self.pagesize,
                }

        request = self.factory.post('/', data)
        request.user = self.user

        response = CreatePatternView.as_view()(request)

        self.assertEqual(response.status_code, 302)

    def test_pattern_get(self):
        request = self.factory.get('/prescription/create_prescription_model/')
        request.user = self.user

        # Get the response
        response = self.my_view.get(request)
        self.assertEqual(response.status_code, 200)
