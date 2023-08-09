from django.urls import path
from account.views import register_user, edit_user, user_login, show_profile, user_logout, add_project, \
    PortfolioProjectDetailView

app_name = 'account'

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/<int:pk>', show_profile, name='profile'),
    path('profile/edit/', edit_user, name='edit_user'),
    path('profile/add_project', add_project, name='add_project'),
    path('profile/show_project/<int:pk>', PortfolioProjectDetailView.as_view(), name='show_project'),
]