from django.contrib import admin
from django.contrib.auth.models import Group, User
from account.models import Profile, PortfolioProject, Role


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


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    prepopulated_fields = {'slug': ('name',)}

