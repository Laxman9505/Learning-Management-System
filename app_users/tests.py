from django.test import TestCase,SimpleTestCase,Client
from django.urls import reverse, resolve
from app_users.views import register, user_login, user_logout
from django.contrib.auth.models import User


class TestUrls(SimpleTestCase):

    databases='__all__'
    def test_register_url(self):
        user = User.objects.create(username='test12')
        user.set_password('1234')
        user.save()
        client = Client()
        logged_in = client.login(username="test12", password="1234")
        response = client.get(reverse(register))
        self.assertEquals(response.status_code, 200)
    def test_register_Read(self):
        user = User.objects.create(username='test123')
        user.set_password('1234')
        user.save()
        client = Client()
        logged_in = client.login(username="test123", password="1234")
        response = client.get(reverse(register))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_users/registration.html')

    def test_login_url(self):
        url = reverse(user_login)
        response = self.assertEquals(resolve(url).func, user_login)
        self.assertTemplateUsed(response, 'app_users/registration.html')

    def test_login_Create(self):
        url = reverse(user_login)
        self.assertEquals(resolve(url).func, user_login)

    def test_logout_url(self):
        url = reverse(user_logout)
        self.assertEquals(resolve(url).func, user_logout)
    
    
