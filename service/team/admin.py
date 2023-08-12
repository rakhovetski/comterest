from django.contrib import admin

from team.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['title', ]

