from django.contrib import admin
from django.contrib.auth.models import Group, User
from account.models import Profile, PortfolioProject, Role
from team.models import Team

admin.site.unregister(Group)
admin.site.unregister(User)


class PortfolioProjectInline(admin.TabularInline):
    model = PortfolioProject
    extra = 1


class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username', 'last_name', 'first_name']
    ordering = ('last_name', )
    search_fields = ['last_name', 'username', 'email']
    inlines = [ProfileInline, PortfolioProjectInline]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_filter = ['experience']
    list_display = ['user', 'experience']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    ordering = ('name', )
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


class RoleInline(admin.TabularInline):
    model = PortfolioProject.role.through
    extra = 1


@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    inlines = [RoleInline]

