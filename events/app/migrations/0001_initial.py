# Generated by Django 3.2.7 on 2021-09-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('event_date', models.DateTimeField(verbose_name='Event Date')),
                ('vanue', models.CharField(max_length=120)),
                ('manager', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
