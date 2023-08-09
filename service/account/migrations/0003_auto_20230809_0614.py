# Generated by Django 3.2.16 on 2023-08-09 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_portfolioproject_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile_images/'),
        ),
        migrations.AlterField(
            model_name='portfolioproject',
            name='role',
            field=models.ManyToManyField(choices=[(1, 'Backend'), (2, 'Frontend'), (3, 'Swift'), (4, 'Python'), (5, 'Docker')], related_name='portfolio_roles', to='account.Role'),
        ),
    ]