# Generated by Django 4.0.4 on 2022-06-25 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='info',
            new_name='bio',
        ),
    ]