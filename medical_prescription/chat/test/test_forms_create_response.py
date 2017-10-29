from django.test import TestCase
from chat.forms import CreateResponse
from user.models import User


class TesteCreateResponseForm(TestCase):

    def setUp(self):
        user = User()
        user.email = "test@test.com"
        user.save()

        self.form_class = CreateResponse
        self.subject = "a"
        self.text = "a"
        self.email = user.email
        self.subject_max = 'a'*1000
        self.text_max = 'a'*1000
        self.email_invalid = 'a2d'

    def test_valid(self):
        form_data = {
                     'text': self.text,
                     'user_to': self.email
                     }
        form = self.form_class(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_text(self):
        form_data = {'text': self.text_max}
        form = self.form_class(data=form_data)
        self.assertFalse(form.is_valid())
