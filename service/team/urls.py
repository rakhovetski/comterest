from django.urls import path

from team.views import add_team, edit_team, delete_team, show_team

app_name = 'team'


urlpatterns = [
    path('add/', add_team, name='add_team'),
    path('edit/<int:pk>/', edit_team, name='edit_team'),
    path('delete/<int:pk>/', delete_team, name='delete_team'),
    path('<int:pk>/', show_team, name='show_team'),
]