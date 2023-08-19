from django.urls import path, include

from api.views import RoleListView, RoleUpdateDestroyView, UserUpdateDeleteView, UserListView, ProfileListView, \
    ProfileDetailView, PortfolioProjectListView, PortfolioProjectDetailView, TeamListView, TeamDetailView
from rest_framework.routers import DefaultRouter


app_name = 'api'


router = DefaultRouter()
router.register(r'profiles', ProfileDetailView, basename='profile')
router.register(r'teams', TeamDetailView, basename='team')


urlpatterns = [
    path('roles/', RoleListView.as_view(), name='roles'),
    path('roles/<int:pk>/', RoleUpdateDestroyView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserUpdateDeleteView.as_view()),
    path('profiles/', ProfileListView.as_view()),
    path('projects/', PortfolioProjectListView.as_view()),
    path('projects/<int:pk>/', PortfolioProjectDetailView.as_view()),
    path('teams/', TeamListView.as_view()),
]

urlpatterns += router.urls
