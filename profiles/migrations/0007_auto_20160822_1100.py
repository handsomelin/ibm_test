# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-22 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20160820_0836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': (('can_edit_base_profile', 'Can edit base profile'), ('can_view_base_profile', 'Can view base profile'))},
        ),
    ]