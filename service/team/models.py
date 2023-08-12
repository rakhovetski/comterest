from django.db import models

from account.models import Profile, Role


class Team(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=5000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.ManyToManyField(Profile, related_name='teams')
    role = models.ManyToManyField(Role, related_name='teams')
    owner = models.ForeignKey(Profile, related_name='owned_teams', on_delete=models.PROTECT, default=None)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = 'команды'
        ordering = ['title']

    def __str__(self):
        return self.title

