from django.test import TestCase
from chat.forms import CreateMessage
from user.models import HealthProfessional, Patient, AssociatedHealthProfessionalAndPatient
from django.core.files.uploadedfile import SimpleUploadedFile


class TestCreateMessageForm(TestCase):

    def setUp(self):
        self.health_professional = HealthProfessional()
        self.health_professional.email = "hp@hp.com"
        self.health_professional.pk = 0
        self.health_professional.save()

        self.patient = Patient()
        self.patient.email = "pt@pt.com"
        self.patient.save()

        self.link = AssociatedHealthProfessionalAndPatient()
        self.link.associated_health_professional = self.health_professional
        self.link.associated_patient = self.patient
        self.link.is_active = True
        self.link.save()

        self.not_linked_patient = Patient.objects.create(email="not_linked@patient.com")

        self.subject = "a"
        self.text = "a"
        self.subject_max = 'a'*1000
        self.text_max = 'a'*1000
        self.email_invalid = 'a2d'

    def test_valid(self):
        upload_file = open('public/image_profile/user.png', 'rb')
        file_dict = {'file': SimpleUploadedFile(upload_file.name, upload_file.read())}
        form_data = {'subject': self.subject,
                     'text': self.text,
                     'files': file_dict,
                     'user_to': self.patient.email,
                     }
        form = CreateMessage(data=form_data)
        self.assertTrue(form.is_valid())

    def test_chat_invalid_subject(self):
        form_data = {'subject': self.subject_max,
                     'text': self.text,
                     'user_to': self.patient.email,
                     'pk': self.health_professional.pk
                     }
        form = CreateMessage(data=form_data)
        self.assertFalse(form.is_valid())

    def test_chat_invalid_text(self):
        form_data = {'subject': self.subject,
                     'text': self.text_max,
                     'user_to': self.patient.email,
                     }
        form = CreateMessage(data=form_data)
        self.assertFalse(form.is_valid())

    def test_chat_invalid_email(self):
        form_data = {'subject': self.subject,
                     'text': self.text,
                     'user_to': self.email_invalid,
                     }
        form = CreateMessage(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_email_health_professional(self):
        form_data = {'subject': self.subject,
                     'text': self.text,
                     'user_to': self.health_professional.email,
                     }
        form = CreateMessage(data=form_data)
        self.assertFalse(form.is_valid())

    def test_link_does_not_exists(self):
        form_data = {'subject': self.subject,
                     'text': self.text,
                     'user_to': self.not_linked_patient.email,
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
