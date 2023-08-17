from rest_framework import generics

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from account.models import Role, Profile, PortfolioProject
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from api.permissions import IsAdminOrReadOnly, IsOwnerOrNothing
from api.serializers import RoleSerializer, UserDetailSerializer, UserSerializer, ProfileDetailSerializer, \
    ProfileSerializer, PortfolioProjectDetailSerializer, PortfolioProjectSerializer, TeamSerializer, \
    TeamDetailSerializer
from team.models import Team


class UserUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAdminUser | IsOwnerOrNothing]


class UserListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    pagination_class = UserListPagination


class RoleListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'name']
    permission_classes = [IsAuthenticated]


class RoleUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdminOrReadOnly]


class PortfolioProjectListView(generics.ListAPIView):
    queryset = PortfolioProject.objects.all()
    serializer_class = PortfolioProjectSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'title', 'created_at']
    permission_classes = [IsAuthenticated]


class PortfolioProjectDetailView(generics.RetrieveAPIView):
    queryset = PortfolioProject.objects.all()
    serializer_class = PortfolioProjectDetailSerializer
    permission_classes = [IsAdminUser | IsOwnerOrNothing]


class TeamListView(generics.ListAPIView):
    queryset = Team.objects.filter(is_active=True)
    serializer_class = TeamSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'title']
    permission_classes = [IsAuthenticated]


class TeamDetailView(mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer
    permission_classes = [IsAdminUser | IsOwnerOrNothing]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'last_name', 'username']
    pagination_class = ProfileListPagination


class ProfileDetailView(mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    permission_classes = [IsAdminUser | IsOwnerOrNothing]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)





