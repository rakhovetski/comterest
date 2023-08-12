from django.urls import path
from search.views import search, profile_list, RoleListView, team_list, home

app_name = 'search'


urlpatterns = [
    path('profile_list/<slug:filter_slug>/', profile_list, name='profile_list'),
    path('profile_list/', profile_list, name='profile_list'),
    path('teams/', team_list, name='teams'),
    path('teams/<int:pk>/', team_list, name='teams'),
    path('roles_list/', RoleListView.as_view(), name='roles_list'),
    path('search/', search, name='search'),
    path('', home, name='home'),
]