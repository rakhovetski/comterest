# Generated by Django 3.2.16 on 2023-08-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioproject',
            name='role',
            field=models.ManyToManyField(choices=[], related_name='portfolio_roles', to='account.Role'),
        ),
    ]