# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-17 09:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0013_migrate_public_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cluster',
            name='public_key',
        ),
    ]
