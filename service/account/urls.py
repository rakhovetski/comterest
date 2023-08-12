from django.urls import path
from account.views import register_user, edit_user, user_login, show_profile, user_logout, add_project, \
    PortfolioProjectDetailView, add_team, edit_project, edit_team, delete_project, delete_team, show_team

app_name = 'account'

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('<int:pk>/', show_profile, name='profile'),
    path('edit/', edit_user, name='edit_user'),
    path('add_project/', add_project, name='add_project'),
    path('show_project/<int:pk>/', PortfolioProjectDetailView.as_view(), name='show_project'),
    path('edit_project/<int:pk>/', edit_project, name='edit_project'),
    path('delete_project/<int:pk>/', delete_project, name='delete_project'),
    path('add_team/', add_team, name='add_team'),
    path('show_team/<int:pk>/', show_team, name='show_team'),
    path('edit_team/<int:pk>/', edit_team, name='edit_team'),
    path('delete_team/<int:pk>/', delete_team, name='delete_team')
]