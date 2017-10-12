
from django.test import TestCase
from exam.models import Exam
from django.test.client import RequestFactory

from exam.views import ListExams


class TestListExam(TestCase):
    def setUp(self):
        self.resp = self.client.get('/exam/list_exams/')
        self.factory = RequestFactory()
        self.my_view = ListExams()

    def test_get_list_exam(self):
        self.assertTrue('list_exam' in self.resp.context)

    def test_get_list_exams(self):
        self.assertFalse('list_exams' in self.resp.context)
