from django.test import TestCase

from prescription.forms import RecommendationPrescriptionForm
from user.models import User


class TestFormRecommendationPrescription(TestCase):
    def setUp(self):
        self.user = User()
        self.user.email = 'email@email.com'
        self.user.save()
        self.user_creator = self.user

        self.recommendation_valid = "teste"
        self.recommendation_invalid = "a"*300

    def test_form_is_valid(self):
        form_data = {
                'recommendation': self.recommendation_valid
                }

        form = RecommendationPrescriptionForm(data=form_data)
        self.assertTrue(form.is_valid())
