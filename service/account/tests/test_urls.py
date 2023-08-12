from django.test import SimpleTestCase
from django.urls import reverse, resolve
from account.views import *


class TestUrls(SimpleTestCase):
    def test_register_url_resolves(self):
        url = reverse('account:register')
        self.assertEquals(resolve(url).func, register_user)

    def test_login_url_resolves(self):
        url = reverse('account:login')
        self.assertEquals(resolve(url).func, user_login)

    def test_logout_url_resolves(self):
        url = reverse('account:logout')
        self.assertEquals(resolve(url).func, user_logout)

    def test_show_profile_url_resolves(self):
        url = reverse('account:profile', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, show_profile)

    def test_edit_user_url_resolves(self):
        url = reverse('account:edit_user')
        self.assertEquals(resolve(url).func, edit_user)

    def test_add_project_url_resolves(self):
        url = reverse('account:add_project')
        self.assertEquals(resolve(url).func, add_project)

    def test_show_project_url_resolves(self):
        url = reverse('account:show_project', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, PortfolioProjectDetailView)

    def test_edit_project_profile_url_resolves(self):
        url = reverse('account:edit_project', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, edit_project)

    def test_delete_project_profile_url_resolves(self):
        url = reverse('account:delete_project', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, delete_project)
