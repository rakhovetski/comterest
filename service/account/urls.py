from django.urls import path, include
from account.views import register_user, edit_user, user_login, show_profile, user_logout, add_project, \
    PortfolioProjectDetailView, edit_project, delete_project
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

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

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change/password_change_done.html'),
         name='password_change_done'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='account/password_change/password_change.html',
                                               success_url=reverse_lazy('account:password_change_done')),
         name='password_change'),
    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_change/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(success_url=reverse_lazy('account:password_reset_done')),
         name='password_reset'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password_change/password_reset_complete.html'),
         name='password_reset_complete'),

    path('team/', include('team.urls', namespace='team')),
]
