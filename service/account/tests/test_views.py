from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from account.models import *
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register = reverse('account:register')
        self.login = reverse('account:login')
        self.logout = reverse('account:logout')
        self.detail_profile = reverse('account:profile', kwargs={'pk': 1})
        self.edit_user = reverse('account:edit_user')
        self.add_project = reverse('account:add_project')
        self.show_project = reverse('account:show_project', kwargs={'pk': 1})
        self.edit_project = reverse('account:edit_project', kwargs={'pk': 1})
        self.delete_project = reverse('account:delete_project', kwargs={'pk': 1})

    def test_register_user_GET(self):
        response = self.client.get(self.register)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register/register.html')

    def test_register_user_POST_all_correct_fields(self):
        response = self.client.post(self.register, {
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email@mail.ru',
            'password1': 'test1234',
            'password2': 'test1234'
        })

        self.assertEquals(response.status_code, 200)

    def test_login_user_GET(self):
        response = self.client.get(self.login)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login/login.html')

    def test_login_user_POST(self):
        response = self.client.post(self.login, {
            'username': 'login',
            'password': 'password123'
        })

        self.assertEquals(response.status_code, 302)

    def test_logout_user_GET(self):
        response = self.client.get(self.logout)

        self.assertEquals(response.status_code, 302)

    def test_show_profile_user_is_not_authenticated_GET(self):
        response = self.client.get(self.detail_profile)

        self.assertEquals(response.status_code, 302)
