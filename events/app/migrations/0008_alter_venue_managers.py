# Generated by Django 3.2.7 on 2021-10-04 07:33

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_vanue_event_venue'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='venue',
            managers=[
                ('venues', django.db.models.manager.Manager()),
            ],
        ),
    ]
