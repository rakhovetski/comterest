from django.urls import path, include
from account.views import register_user, edit_user, user_login, show_profile, user_logout, add_project, \
    PortfolioProjectDetailView, edit_project, delete_project

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

    path('team/', include('team.urls', namespace='team')),
]