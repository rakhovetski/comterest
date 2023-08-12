from django.test import SimpleTestCase
from django.urls import reverse, resolve
from search.views import *


class TestUrls(SimpleTestCase):

    def test_profile_list_urls_resolves(self):
        url = reverse('search:profile_list', kwargs={'filter_slug': 'backend'})
        self.assertEquals(resolve(url).func, profile_list)

    def test_profile_list_urls_with_slug_filter_resolves(self):
        url = reverse('search:profile_list')
        self.assertEquals(resolve(url).func, profile_list)

    def test_teams_list_urls_resolves(self):
        url = reverse('search:teams')
        self.assertEquals(resolve(url).func, team_list)

    def test_teams_list_urls_by_pk_resolves(self):
        url = reverse('search:teams', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, team_list)

    def test_roles_list_urls_resolves(self):
        url = reverse('search:roles_list')
        self.assertEquals(resolve(url).func.view_class, RoleListView)

