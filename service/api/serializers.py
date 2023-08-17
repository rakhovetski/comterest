from rest_framework import serializers
from django.contrib.auth.models import User

from account.models import Profile, PortfolioProject, Role
from team.models import Team


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', )


class PortfolioProjectDetailSerializer(serializers.ModelSerializer):
    role = RoleSerializer(many=True)

    class Meta:
        model = PortfolioProject
        fields = ['id', 'title', 'description', 'role', 'user_id']


class PortfolioProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioProject
        fields = ['id', 'title', 'description', 'formatted_date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_name', 'first_name', )


class UserDetailSerializer(serializers.ModelSerializer):
    portfolio_projects = PortfolioProjectDetailSerializer(many=True)

    class Meta:
        model = User
        exclude = ('password', )


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'experience']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['title', 'description', 'formatted_date']


class TeamDetailSerializer(serializers.ModelSerializer):
    role = RoleSerializer(many=True)
    profile = ProfileSerializer(many=True)
    owner = ProfileSerializer()

    class Meta:
        model = Team
        fields = ['title', 'description', 'created_at',
                  'profile', 'role', 'owner',
                  'is_active']


class ProfileDetailSerializer(serializers.ModelSerializer):
    follows = serializers.PrimaryKeyRelatedField(many=True,
                                                 queryset=Profile.objects.all())
    user = UserDetailSerializer()

    class Meta:
        model = Profile
        exclude = ['updated_date', 'profile_image']
