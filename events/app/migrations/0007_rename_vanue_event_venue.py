# Generated by Django 3.2.7 on 2021-09-29 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_event_manager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='vanue',
            new_name='venue',
        ),
    ]
