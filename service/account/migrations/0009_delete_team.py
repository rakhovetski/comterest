# Generated by Django 3.2.16 on 2023-08-12 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_profile_date_of_birth'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Team',
        ),
    ]