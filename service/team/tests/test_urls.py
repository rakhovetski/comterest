from django.urls import reverse, resolve
from team.views import *
from django.test import SimpleTestCase


class TestUrls(SimpleTestCase):

    def test_add_team_url_resolves(self):
        url = reverse('account:team:add_team')
        self.assertEquals(resolve(url).func, add_team)

    def test_edit_team_url_resolves(self):
        url = reverse('account:team:edit_team', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, edit_team)

    def test_delete_team_url_resolves(self):
        url = reverse('account:team:delete_team', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, delete_team)

    def test_show_team_url_resolves(self):
        url = reverse('account:team:show_team', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, show_team)
