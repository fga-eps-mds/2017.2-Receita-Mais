from django.test import TestCase
from chat.forms import CreateMessage
from user.models import User, HealthProfessional
from django.core.files.uploadedfile import SimpleUploadedFile


class TestCreateMessageForm(TestCase):

    def setUp(self):
        user = User()
        user.email = "test@test.com"
        user.save()

        health_professional = HealthProfessional()
        health_professional.email = "hp@hp.com"
        health_professional.save()

        self.subject = "a"
        self.text = "a"
        self.email = user.email
        self.subject_max = 'a'*1000
        self.text_max = 'a'*1000
        self.email_invalid = 'a2d'
        self.email_health_professional = health_professional.email

    def test_valid(self):
        upload_file = open('public/image_profile/user.png', 'rb')
        file_dict = {'file': SimpleUploadedFile(upload_file.name, upload_file.read())}
        form_data = {'subject': self.subject,
                     'text': self.text,
                     'files': file_dict,
                     'user_to': self.email
                     }
        form = CreateMessage(data=form_data)
        self.assertTrue(form.is_valid())

    def test_chat_invalid_subject(self):
        form_data = {'subject': self.subject_max,
                     'text': self.text,
                     }
        form = CreateMessage(data=form_data)
        self.assertFalse(form.is_valid())

    def test_chat_invalid_text(self):
        form_data = {'subject': self.subject,
                     'text': self.text_max,
                     'user_to': self.email,
                     }
        form = CreateMessage(data=form_data)
        self.assertFalse(form.is_valid())

    def test_chat_invalid_email(self):
        form_data = {'subject': self.subject,
                     'text': self.text,
                     'user_to': self.email_invalid
                     }
        form = CreateMessage(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_email_health_professional(self):
        form_data = {'subject': self.subject,
                     'text': self.text,
                     'user_to': self.email_health_professional
                     }
        form = CreateMessage(data=form_data)
        self.assertFalse(form.is_valid())

    def test_chat_invalid_subject_None(self):
        form_data = {'subject': None,
                     'text': self.text,
                     'user_to': self.email_invalid
                     }
        form = CreateMessage(data=form_data)
        self.assertFalse(form.is_valid())

    def test_chat_invalid_text_None(self):
        form_data = {'subject': self.subject,
                     'text': None,
                     'user_to': self.email_invalid
                     }
        form = CreateMessage(data=form_data)
        self.assertFalse(form.is_valid())
