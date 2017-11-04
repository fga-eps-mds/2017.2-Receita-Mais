# Django
from django.test import TestCase
from django.test.client import RequestFactory

# Django Local
from recommendation.forms import CreateRecomendationCustomForm
from recommendation.models import CustomRecommendation
from user.models import HealthProfessional


class CreateRecomendationCustomFormTeste(TestCase):
    def setUp(self):
        self.name_valid = "Diabetes"
        self.name_valid_duplicate = "Diabetes Dois"
        self.name_invalid_min = "A"
        self.name_invalid_max = """NomeinvalidoNomeinvalidoNomeinvalidoNomeinvalidoNomeinvalidoNomeinvalidoNomeinvalido
        NomeinvalidoNomeinvalidoNomeinvalidoNomeinvalidoNomeinvalidoNomeinvalidoNomeinvalidoNomeinvalidoNomeinvalido"""
        self.description_valid = "Alguma descrição aceitavel"
        self.description_invalid_min = "A"
        self.description_invalid_max = """adjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihai
        ufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuah
        adjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihaiufdha
        ihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhf
        iahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiu
        hfiuahfidhfiahiudfhaiufhdiuah"""

        self.health_professional = HealthProfessional()
        self.health_professional.pk = 1
        self.health_professional.crm = '12345'
        self.health_professional.crm_state = 'US'
        self.health_professional.save()

        self.custom_recomendation = CustomRecommendation()
        self.custom_recomendation.name = self.name_valid_duplicate
        self.custom_recomendation.description = self.description_valid
        self.custom_recomendation.health_professional = self.health_professional
        self.custom_recomendation.save()

        self.factory = RequestFactory()
        self.request = self.factory.get('/recommendation/create_custom')
        self.request.user = self.health_professional

    def test_custom_recommendation_form_valid(self):
        form_data = {'name': self.name_valid,
                     'description': self.description_valid}
        form = CreateRecomendationCustomForm(data=form_data)
        form.get_request(self.request)

        self.assertTrue(form.is_valid())

    def test_custom_recommendation_form_invalid_description_min(self):
        form_data = {'name': self.name_valid,
                     'description': self.description_invalid_min}
        form = CreateRecomendationCustomForm(data=form_data)
        form.get_request(self.request)

        self.assertFalse(form.is_valid())

    def test_custom_recommendation_form_invalid_name_min(self):
        form_data = {'name': self.name_invalid_min,
                     'description': self.description_valid}
        form = CreateRecomendationCustomForm(data=form_data)
        form.get_request(self.request)

        self.assertFalse(form.is_valid())

    def test_custom_recommendation_form_invalid_name_max(self):
        form_data = {'name': self.name_invalid_max,
                     'description': self.description_valid}
        form = CreateRecomendationCustomForm(data=form_data)
        form.get_request(self.request)

        self.assertFalse(form.is_valid())

    def test_custom_recommendation_form_invalid_description_max(self):
        form_data = {'name': self.name_valid,
                     'description': self.description_invalid_max}
        form = CreateRecomendationCustomForm(data=form_data)
        form.get_request(self.request)

        self.assertFalse(form.is_valid())

    def test_custom_recommendation_form_invalid_name_duplicate(self):
        form_data = {'name': self.name_valid_duplicate,
                     'description': self.description_valid}
        form = CreateRecomendationCustomForm(data=form_data)
        form.get_request(self.request)

        self.assertFalse(form.is_valid())
