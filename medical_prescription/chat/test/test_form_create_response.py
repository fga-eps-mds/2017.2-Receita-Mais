from django.test import TestCase
from chat.forms import CreateResponse
from user.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


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

        im = Image.new(mode='RGB', size=(200, 200))  # create a new image using PIL
        im_io = BytesIO()  # a StringIO object for saving image
        im.save(im_io, 'JPEG')  # save the image to im_io
        im_io.seek(0)  # seek to the beginning

        image = InMemoryUploadedFile(
            im_io, None, 'random-name.jpg', 'image/jpeg', im_io, None
        )

        file_dict = {'files': image}

        form_data = {
                     'text': self.text,
                     'user_to': self.email,
                     'files': file_dict
                     }
        form = self.form_class(data=form_data)
        self.assertTrue(form.is_valid())

    def test_chat_invalid_text(self):
        form_data = {'text': self.text_max}
        form = self.form_class(data=form_data)
        self.assertFalse(form.is_valid())
