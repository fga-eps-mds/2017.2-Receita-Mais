
from django.test import TestCase

from chat.forms import CreateMessage
from user.models import User


class TestCreateMessageForm(TestCase):
    def setUp(self):
        user = User()
        user.email = "test@test.com"
        user.save()

        self.subject = "a"
        self.text = "a"
        self.email = user.email
        self.subject_max = 'a'*1000
        self.text_max = 'a'*1000
        self.email_invalid = 'a2d'

    def test_valid(self):
        form_data = {'subject': self.subject,
                     'text': self.text,
                     'user_to': self.email
                     }
        form = CreateMessage(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_subject(self):
        form_data = {'subject': self.subject_max,
                     'text': self.text,
                     }
        form = CreateMessage(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_text(self):
        form_data = {'subject': self.subject,
                     'text': self.text_max,
                     }
        form = CreateMessage(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        form_data = {'subject': self.subject,
                     'text': self.text,
                     'user_to': self.email_invalid
                     }
        form = CreateMessage(data=form_data)
        self.assertFalse(form.is_valid())
