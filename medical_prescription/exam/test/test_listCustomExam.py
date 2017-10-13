
from django.test import TestCase
from django.test.client import RequestFactory

from exam.views import ListCustomExams


class TestListCustomExam(TestCase):
    def setUp(self):
        self.resp = self.client.get('/exam/list_custom_exams/')
        self.factory = RequestFactory()
        self.my_view = ListCustomExams()

    def test_get_list_exam(self):
        self.assertTrue('list_custom_exam' in self.resp.context)

    def test_get_list_exams(self):
        self.assertFalse('list_custom_exams' in self.resp.context)
