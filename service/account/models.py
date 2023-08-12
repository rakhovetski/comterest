from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save


class Role(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'роль'
        verbose_name_plural = 'роли'

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.PositiveIntegerField(null=True, blank=True, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    follows = models.ManyToManyField('self',
                                     related_name='followed_by',
                                     symmetrical=False,
                                     blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/profile_images/')

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def full_name(self):
        return f'{self.user.last_name} {self.user.first_name}'

    def roles_by_profile(self):
        roles = set()
        projects = self.user.portfolio_projects.all()

        for project in projects:
            for role in project.role.all():
                roles.add(role)
        return roles

    def __str__(self):
        return f'{self.user.username}: {self.full_name()}'


def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


post_save.connect(create_profile, sender=User)


class PortfolioProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='portfolio_projects')
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=5000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.ManyToManyField(Role, related_name='portfolio_roles')

    class Meta:
        verbose_name = 'проект в портфолио'
        verbose_name_plural = 'проекты в портфолио'
        ordering = ['title']

    def formatted_date(self):
        return self.created_at.strftime('%B %d %Y')

    def __str__(self):
        return f'{self.user} - {self.title} - {self.formatted_date()}'




