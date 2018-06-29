import os
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

# Create your tests here.
class UserModelTest(TestCase):

    def test_string_representation(self):
        username="trungnt"
        email="trungnt@socicom.vn"
        user = User(username=username, email=email)
        self.assertEqual(str(user), user.username)

class AdminTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="admin", email="trungnt@icts.vn", is_staff=True, is_superuser=True)
        user.set_password('123456')
        user.save()

    def test_login_fail(self):
        c = Client()
        c.login(username='admin', password='1234562')
        self.assertEqual(c.get('/admin/').status_code, 302)

    def test_login(self):
        c = Client()
        c.login(username='admin', password='123456')
        self.assertEqual(c.get('/admin/').status_code, 200)

    def test_admin_header(self):
        self.client.login(username='admin', password='123456')
        res = self.client.get('/admin/')
        self.assertContains(res, os.environ.get('ADMIN_SITE_HEADER') or 'Django administration', status_code=200)
