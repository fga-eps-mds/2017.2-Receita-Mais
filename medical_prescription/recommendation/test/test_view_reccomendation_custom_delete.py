from django.test import TestCase, RequestFactory, Client
from recommendation.views import CustomRecommendationDeleteView
from recommendation.models import CustomRecommendation

from user.models import HealthProfessional


class TestArchiveMessageOutboxView(TestCase):

    def setUp(self):

        self.user = HealthProfessional.objects.create(name='User Test',
                                                      email='test@teste.com',
                                                      sex='M',
                                                      phone='1111111111',
                                                      is_active=True)
        self.view = CustomRecommendationDeleteView()
        self.view_class = CustomRecommendationDeleteView
        self.factory = RequestFactory()
        self.client = Client()
        # Create Message.

        self.recommendation = CustomRecommendation()
        self.recommendation.name = "meu texto"
        self.recommendation.recommendation = "Assunto"
        self.recommendation.health_professional = self.user
        self.recommendation.is_active = True
        self.recommendation.pk = '1'
        self.recommendation.save()

    def test_post_true(self):
        request = self.factory.post('/')

        request.user = self.user
        self.view.request = request
        self.view.object = self.recommendation

        recommendation = self.view_class.post(request, pk=1)
        self.assertEqual(recommendation.status_code, 302)
