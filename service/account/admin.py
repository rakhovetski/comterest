from django.contrib import admin
from django.contrib.auth.models import Group, User
from account.models import Profile, PortfolioProject, Role, ProfileTeam, Team


admin.site.unregister(Group)
admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]


admin.site.register(User, UserAdmin)
admin.site.register(Profile)

admin.site.register(PortfolioProject)


# class PortfolioProjectInline(admin.TabularInline):
#     model = PortfolioProject
#     extra = 1
#
#
# class ProfileTeamInline(admin.StackedInline):
#     model = ProfileTeam
#     extra = 1
#
#
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['username', 'last_name', 'first_name', 'email']
#     list_filter = ['experience', ]
#     search_fields = ['phone', 'email', 'last_name']
#     inlines = [PortfolioProjectInline, ProfileTeamInline]
#
#
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    prepopulated_fields = {'slug': ('name',)}
#
#
# @admin.register(Team)
# class TeamAdmin(admin.ModelAdmin):
#     list_display = ['title', ]
#     inlines = [ProfileTeamInline]
#
#
# @admin.register(ProfileTeam)
# class ProfileTeamAdmin(admin.ModelAdmin):
#     list_display = ['profile', 'team']
#
#
# @admin.register(PortfolioProject)
# class PortfolioProjectAdmin(admin.ModelAdmin):
#     list_display = ['title', 'git_url']


