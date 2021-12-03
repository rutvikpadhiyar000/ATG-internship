# Generated by Django 3.2.9 on 2021-12-03 04:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Eid', models.CharField(blank=True, max_length=50, verbose_name='Event id')),
                ('summary', models.CharField(max_length=120, verbose_name='Title')),
                ('organizer', models.CharField(blank=True, max_length=50, verbose_name='Organizer of event ')),
                ('start_time', models.DateTimeField(verbose_name='Event start time')),
                ('end_time', models.DateTimeField(verbose_name='Event end time')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('attendees', models.CharField(blank=True, default=' ', help_text='enter attendees separated by a comma ', max_length=1000, verbose_name='Attendees')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]