
from django.test import TestCase

from exam.forms import UpdateCustomExamForm
from exam.models import CustomExam
from user.models import HealthProfessional


class TestCreateCustomExamForm(TestCase):
    def setUp(self):
        self.my_view = UpdateCustomExamForm()
        self.name_min = None
        self.name_valid = "Alguma coisa"
        self.name_exists = "Invalido"

        self.description_max = """adjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihai
        ufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuah
        adjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihaiufdha
        ihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhf
        iahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiu
        hfiuahfidhfiahiudfhaiufhdiuah"""

        self.name_max = """adjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihai
        ufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuah
        adjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihaiufdha
        ihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhf
        iahdfiahdufhaisdhfiuahdfuihaiufdhaihfiuhfiuahfidhfiahiudfhaiufhdiuahadjhfiahdfiahdufhaisdhfiuahdfuihaiufdhaihfiu
        hfiuahfidhfiahiudfhaiufhdiuah"""

        self.description_min = "as"
        self.description_valid = "Examina alguma coisa"

        custom_exam = CustomExam()
        custom_exam.name = "Invalido"
        user = HealthProfessional()
        user.crm = "54321"
        user.save()
        custom_exam.health_professional_FK = user
        custom_exam.pk = 1
        custom_exam.save()

    def teste_exam_valid(self):
        form_data = {'name': self.name_valid,
                     'description': self.description_valid
                     }
        form = UpdateCustomExamForm(data=form_data)
        form.get_pk(1)
        self.assertTrue(form.is_valid())

    def test_invalid_max_name(self):
        form_data = {'name': self.name_max,
                     'description': self.description_valid
                     }
        form = UpdateCustomExamForm(data=form_data)
        form.get_pk(1)
        self.assertFalse(form.is_valid())

    def test_invalid_min_name(self):
        form_data = {'name': self.name_min,
                     'description': self.description_valid
                     }
        form = UpdateCustomExamForm(data=form_data)
        form.get_pk(1)
        self.assertFalse(form.is_valid())

    def test_invalid_max_description(self):
        form_data = {'name': self.name_valid,
                     'description': self.description_max
                     }
        form = UpdateCustomExamForm(data=form_data)
        form.get_pk(1)
        self.assertFalse(form.is_valid())

    def test_invalid_min_description(self):
        form_data = {'name': self.name_valid,
                     'description': self.description_min
                     }
        form = UpdateCustomExamForm(data=form_data)
        form.get_pk(1)
        self.assertFalse(form.is_valid())
