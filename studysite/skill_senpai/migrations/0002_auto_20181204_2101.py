# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-12-04 21:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill_senpai', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subject',
            new_name='Lecture',
        ),
    ]