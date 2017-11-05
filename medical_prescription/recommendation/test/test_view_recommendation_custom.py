# Django
from django.test import TestCase
from django.test.client import RequestFactory

# Django Local
from recommendation.views import CustomRecommendationCreateView
from user.models import HealthProfessional


class CreateRecomendationCustomViewTeste(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.health_professional = HealthProfessional()
        self.health_professional.pk = 1
        self.health_professional.crm = '12345'
        self.health_professional.crm_state = 'US'
        self.health_professional.save()

    def test_recommendation_get_with_health_professional(self):
        request = self.factory.get('/recommendation/create_custom')
        request.user = self.health_professional

        # Get the response
        response = CustomRecommendationCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_recommendation_post_with_health_professional_valid(self):
        context = {'name': "Diabetes",
                   'description': "Alguma descrição aceitavel"}

        request = self.factory.post('/prescription/create_modal/', context)
        request.user = self.health_professional

        # Get the response
        response = CustomRecommendationCreateView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_recommendation_post_with_health_professional_invalid(self):
        context = {'name': "A",
                   'description': "Alguma descrição aceitavel"}

        request = self.factory.post('/prescription/create_modal/', context)
        request.user = self.health_professional

        # Get the response
        response = CustomRecommendationCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)
