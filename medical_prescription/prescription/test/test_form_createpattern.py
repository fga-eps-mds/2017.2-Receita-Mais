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
        self.user_creator = self.user

        self.name = "Pattern de teste"
        self.clinic = "clinica de teste"
        self.header = "header de teste"
        self.font = 'Helvetica'
        self.font_size = '12'
        self.footer = "footer de teste"
        self.pagesize = "letter"

        self.name_invalid = "a"*300
        self.clinic_invalid = "a"*300
        self.header_invalid = "a"*300
        self.footer_invalid = "a"*300

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

    def test_form_is_invalid_name(self):
        form_data = {
                'name': self.name_invalid,
                'clinic': self.clinic,
                'font': 'Helvetica',
                'font_size': '12',
                'header': self.header,
                'footer': self.footer,
                'pagesize': self.pagesize,
                }

        form = PatternForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_is_invalid_footer(self):
        form_data = {
                'name': self.name,
                'clinic': self.clinic,
                'font': 'Helvetica',
                'font_size': '12',
                'header': self.header,
                'footer': self.footer_invalid,
                'pagesize': self.pagesize,
                }

        form = PatternForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_is_invalid_header(self):
        form_data = {
                'name': self.name,
                'clinic': self.clinic,
                'font': 'Helvetica',
                'font_size': '12',
                'header': self.header_invalid,
                'footer': self.footer,
                'pagesize': self.pagesize,
                }

        form = PatternForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_is_invalid_clinic(self):
        form_data = {
                'name': self.name,
                'clinic': self.clinic_invalid,
                'font': 'Helvetica',
                'font_size': '12',
                'header': self.header,
                'footer': self.footer,
                'pagesize': self.pagesize,
                }

        form = PatternForm(data=form_data)
        self.assertFalse(form.is_valid())
