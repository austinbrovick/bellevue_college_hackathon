# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 06:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.IntegerField(default=0)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_location)),
                ('grade', models.CharField(blank=True, choices=[('Running Start', 'Running Start'), ('Freshman', 'Freshman'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Senior', 'Senior')], max_length=30, null=True)),
                ('major', models.CharField(blank=True, choices=[('Finance', 'Finance'), ('Accounting', 'Accounting'), ('Marketing', 'Marketing'), ('Human Resources', 'Human Resources'), ('Economics', 'Economics'), ('Computer Science', 'Computer Science'), ('English', 'English'), ('History', 'History')], max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
