# Django
from django.test import TestCase
from django.test.client import RequestFactory

# Django Local
from recommendation.views import UpdateCustomRecommendation
from user.models import HealthProfessional
from recommendation.models import CustomRecommendation


class DeleteRecomendationCustomViewTeste(TestCase):
    def setUp(self):
        self.health_professional_1 = HealthProfessional.objects.create_user(email='doctor1@doctor.com',
                                                                            password='senha12')
        self.health_professional_2 = HealthProfessional.objects.create_user(email='doctor2@doctor.com',
                                                                            password='senha12',
                                                                            crm='54321')
        self.custom_recommendation_1 = CustomRecommendation()
        self.custom_recommendation_1.pk = 1
        self.custom_recommendation_1.name = "Testando 1"
        self.custom_recommendation_1.description = "Testa isso direito meu amigo 1"
        self.custom_recommendation_1.health_professional = self.health_professional_1
        self.custom_recommendation_1.save()

        self.custom_recommendation_2 = CustomRecommendation()
        self.custom_recommendation_2.pk = 2
        self.custom_recommendation_2.name = "Testando 2"
        self.custom_recommendation_2.description = "Testa isso direito meu amigo 2"
        self.custom_recommendation_2.health_professional = self.health_professional_1
        self.custom_recommendation_2.save()

        self.custom_recommendation_2 = CustomRecommendation()
        self.custom_recommendation_2.pk = 2
        self.custom_recommendation_2.name = "Testando 3"
        self.custom_recommendation_2.description = "Testa isso direito meu amigo 3"
        self.custom_recommendation_2.health_professional = self.health_professional_2
        self.custom_recommendation_2.save()

        self.view = UpdateCustomRecommendation()
        self.factory = RequestFactory()

    def test_custom_recommendation_edit_get(self):
        request = self.factory.get('/recommendation/update_custom_recommendation/(?P<pk>[0-9]+)/')
        request.user = self.health_professional_1
        response = UpdateCustomRecommendation.as_view()(request, pk=self.custom_recommendation_1.pk)

        self.assertEqual(response.status_code, 200)

    def test_custom_recommendation_edit_post_valid(self):
        context = {'name': "Diabetes",
                   'recommendation': "Alguma descrição aceitavel"}

        request = self.factory.post(
            '/recommendation/update_custom_recommendation/(?P<pk>[0-9]+)/',
            context
            )
        request.user = self.health_professional_1
        response = UpdateCustomRecommendation.as_view()(request, pk=self.custom_recommendation_1.pk)

        self.assertEqual(response.status_code, 302)

    def test_custom_recommendation_edit_post_invalid(self):
        context = {'name': self.custom_recommendation_2.name,
                   'recommendation': "Alguma descrição aceitavel"}

        request = self.factory.post(
            '/recommendation/update_custom_recommendation/(?P<pk>[0-9]+)/',
            context
            )
        request.user = self.health_professional_1
        response = UpdateCustomRecommendation.as_view()(request, pk=self.custom_recommendation_1.pk)

        self.assertEqual(response.status_code, 200)
