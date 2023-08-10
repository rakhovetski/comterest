from django.urls import path
from account.views import register_user, edit_user, user_login, show_profile, user_logout, add_project, \
    PortfolioProjectDetailView, add_team, TeamDetailView, edit_project, edit_team

app_name = 'account'

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/<int:pk>/', show_profile, name='profile'),
    path('profile/edit/', edit_user, name='edit_user'),
    path('profile/add_project/', add_project, name='add_project'),
    path('profile/show_project/<int:pk>/', PortfolioProjectDetailView.as_view(), name='show_project'),
    path('profile/edit_project/<int:pk>/', edit_project, name='edit_project'),
    path('profile/add_team/', add_team, name='add_team'),
    path('profile/show_team/<int:pk>/', TeamDetailView.as_view(), name='show_team'),
    path('profile/edit_team/<int:pk>', edit_team, name='edit_team'),
]