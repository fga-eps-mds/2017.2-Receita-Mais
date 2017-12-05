# Django
from django.test import TestCase
from django.test.client import RequestFactory

# Django Local
from recommendation.views import CustomRecommendationDeleteView
from user.models import HealthProfessional
from recommendation.models import CustomRecommendation


class DeleteRecomendationCustomViewTeste(TestCase):
    def setUp(self):
        self.health_professional_1 = HealthProfessional.objects.create_user(email='doctor1@doctor.com',
                                                                            password='senha12')
        self.health_professional_2 = HealthProfessional.objects.create_user(email='doctor2@doctor.com',
                                                                            password='senha12')
        self.custom_recommendation = CustomRecommendation()
        self.custom_recommendation.pk = 1
        self.custom_recommendation.name = "Testando"
        self.custom_recommendation.description = "Testa isso direito meu amigo"
        self.custom_recommendation.health_professional = self.health_professional
        self.custom_recommendation.save()
        self.view = CustomRecommendationDeleteView()
        self.factory = RequestFactory()

    def post_custom_recommendation_true(self):
        request = self.factory.post('/')

        request.user = self.user
        self.view.request = request
        self.view.object = self.custom_recommendation

        custom_delete = self.view_class.post(request, pk=1)
        self.assertEqual(custom_delete.status_code, 302)
