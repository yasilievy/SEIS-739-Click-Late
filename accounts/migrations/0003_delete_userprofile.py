# Generated by Django 5.1.6 on 2025-03-21 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
