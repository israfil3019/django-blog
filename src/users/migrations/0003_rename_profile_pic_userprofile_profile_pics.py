# Generated by Django 3.2.5 on 2021-07-27 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_userprofile_portfolio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_pic',
            new_name='profile_pics',
        ),
    ]