from django.urls import path, include

from api.views import RoleListView, RoleUpdateDestroyView, UserUpdateDeleteView, UserListView, ProfileListView, \
    ProfileDetailView, PortfolioProjectListView, PortfolioProjectDetailView
from rest_framework.routers import DefaultRouter


app_name = 'api'


router = DefaultRouter()
router.register(r'profiles', ProfileDetailView, basename='profile')


urlpatterns = [
    path('roles/', RoleListView.as_view()),
    path('roles/<int:pk>/', RoleUpdateDestroyView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserUpdateDeleteView.as_view()),
    path('profiles/', ProfileListView.as_view()),
    path('projects/', PortfolioProjectListView.as_view()),
    path('projects/<int:pk>/', PortfolioProjectDetailView.as_view()),
]

urlpatterns += router.urls
