from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser

from user.models import HealthProfessional
from prescription.models import Pattern
from prescription.views import EditPatternView


class TestEditPattern(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = EditPatternView()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com', password='senha12')

        self.pattern = Pattern()
        self.pattern.pk = 1
        self.pattern.name = 'Modelo #1'
        self.pattern.user_creator = self.health_professional
        self.pattern.font = 'Helvetica'
        self.pattern.font_size = '11'
        self.pattern.pagesize = 'letter'
        self.pattern.clinic = 'Clinica de Teste'
        self.pattern.header = 'Cabecalho #1'
        self.pattern.footer = 'Rodape #1'
        self.pattern.logo = None
        self.pattern.save()

    def test_pattern_post(self):
        request = self.factory.post('prescription/edit_pattern/(?P<pk>[0-9]+)',
                                    {'name': self.pattern.name,
                                     'font': self.pattern.font,
                                     'font_size': self.pattern.font_size,
                                     'pagesize': self.pattern.pagesize,
                                     'clinic': self.pattern.clinic,
                                     'header': self.pattern.header,
                                     'footer': self.pattern.footer,
                                     })
        request.user = self.health_professional

        response = EditPatternView.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_pattern_post_without_login(self):
        request = self.factory.post('prescription/edit_pattern/(?P<pk>[0-9]+)',
                                    {'name': self.pattern.name,
                                     'font': self.pattern.font,
                                     'font_size': self.pattern.font_size,
                                     'pagesize': self.pattern.pagesize,
                                     'clinic': self.pattern.clinic,
                                     'header': self.pattern.header,
                                     'footer': self.pattern.footer,
                                     })
        request.user = AnonymousUser()

        response = EditPatternView.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)

    def test_pattern_get_without_login(self):
        request = self.factory.get('prescription/edit_pattern/(?P<pk>[0-9]+)/')
        request.user = AnonymousUser()

        response = EditPatternView.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 302)

    def test_get_url_success(self):
        self.assertEqual(self.view.get_success_url(), '/pt-br/prescription/list_patterns/')
