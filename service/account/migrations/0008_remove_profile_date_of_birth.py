# Generated by Django 3.2.16 on 2023-08-12 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_profile_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
    ]
