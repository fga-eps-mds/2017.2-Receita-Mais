from django.test import TestCase
from chat.models import Response
from user.models import User

from io import BytesIO
from PIL import Image
from django.core.files.base import File


class TestResponseModel(TestCase):

    def setUp(self):
        self.user = User()
        self.user.email = "test@test.com"
        self.user.save()

    @staticmethod
    def get_image_file(name='test.bmp', ext='bmp', size=(50, 50), color=(256, 0, 0)):
        file_obj = BytesIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def test_add_photo(self):
        newResponse = Response()
        newResponse.files = self.get_image_file()
        newResponse.file_name = newResponse.files.name
        newResponse.user_from = self.user
        newResponse.user_to = self.user
        newResponse.text = 'asdad'
        newResponse.save()
        self.assertEqual(Response.objects.count(), 1)
