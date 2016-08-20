# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-18 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('view_task', 'Can see available tasks'), ('change_task_status', 'Can change the status of tasks'), ('close_task', 'Can remove a task by setting its status as closed'))},
        ),
    ]
