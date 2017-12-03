from django.test import TestCase
from django.test.client import RequestFactory, Client

from chat.views import ComposeView
from user.models import HealthProfessional, Patient, AssociatedHealthProfessionalAndPatient


class TestComposeView(TestCase):
    """
    Testing methods of Class ComposeView.
    """
    def setUp(self):

        # Creating user in database.
        self.user = HealthProfessional()
        self.user.email = "test@test.com"
        self.user.save()

        self.patient = Patient()
        self.patient.email = "patient@test.com"
        self.patient.save()

        self.link = AssociatedHealthProfessionalAndPatient()
        self.link.associated_health_professional = self.user
        self.link.associated_patient = self.patient
        self.link.is_active = True
        self.link.save()

        self.not_linked_patient = Patient()
        self.not_linked_patient.email = "not_linked@patient.com"
        self.not_linked_patient.save()

        self.subject = "a"
        self.text = "a"

        self.factory = RequestFactory()
        self.my_view = ComposeView()
        self.my_view_class = ComposeView
        self.client = Client()

    def test_chat_get(self):
        request = self.factory.get('/chat/compose/')
        request.user = self.user
        response = self.my_view.get(request)
        self.assertEqual(response.status_code, 200)

    def test_chat_post(self):
        request = self.factory.post('chat/compose',
                                    {'text': self.text,
                                     'subject': self.subject,
                                     'user_from': self.user.email,
                                     'user_to': self.patient.email
                                     })
        request.user = self.user

        response = self.my_view_class.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_chat_post_invalid_user_to_health_professional(self):
        request = self.factory.post('chat/compose',
                                    {'text': self.text,
                                     'subject': self.subject,
                                     'user_from': self.user.email,
                                     'user_to': self.user.email
                                     })
        request.user = self.user

        response = self.my_view_class.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_chat_post_invalid_user_to_not_linked(self):
        request = self.factory.post('chat/compose',
                                    {'text': 'a'*10000,
                                     'subject': 'test suject',
                                     'user_from': self.user.email,
                                     'user_to': self.not_linked_patient.email
                                     })
        request.user = self.user

        response = self.my_view_class.as_view()(request)
        self.assertEqual(response.status_code, 200)
