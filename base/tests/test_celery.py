from django.test import TestCase
from base.celery import test

from django.contrib.admin.options import (
    ModelAdmin
)

# Create your tests here.


class CeleryTest(TestCase):

    def setUp(self):
        return None

    # def test_test(self):
    #     str = 'hello123'
    #     task = test.s(str=str).delay()
    #     result = task.get()
    #     self.assertEqual(result, str)
    #     self.assertEqual(task.status, 'SUCCESS')
