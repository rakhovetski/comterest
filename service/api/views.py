from rest_framework import generics

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from account.models import Role, Profile
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from api.permissions import IsAdminOrReadOnly, IsOwnerOrNothing
from api.serializers import RoleSerializer, UserDetailSerializer, UserSerializer, ProfileDetailSerializer, \
    ProfileListSerializer


class UserUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAdminUser | IsOwnerOrNothing]


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class RoleListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'name']


class RoleUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'last_name', 'username']


class ProfileDetailView(mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)





