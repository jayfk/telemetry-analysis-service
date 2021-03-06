# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-08 09:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20161102_1049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sparkjob',
            options={'permissions': [('view_sparkjob', 'Can view Spark job')]},
        ),
        migrations.AlterField(
            model_name='sparkjob',
            name='created_by',
            field=models.ForeignKey(help_text=b'User that created the instance.', on_delete=django.db.models.deletion.CASCADE, related_name='created_sparkjobs', to=settings.AUTH_USER_MODEL),
        ),
    ]
