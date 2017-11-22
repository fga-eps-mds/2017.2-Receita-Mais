from django.test import TestCase

from prescription.models import Pattern
from prescription.forms import PatternForm
from prescription.views import CreatePatternView
from user.models import User


class TestFormCreatePattern(TestCase):
    def setUp(self):
        self.user = User()
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

    def test_form_is_valid(self):
        form_data = {
                'name': self.name,
                'clinic': self.clinic,
                'font': 'Helvetica',
                'font_size': '12',
                'header': self.header,
                'footer': self.footer,
                'pagesize': self.pagesize,
                }

        form = PatternForm(data=form_data)
        self.assertTrue(form.is_valid())
