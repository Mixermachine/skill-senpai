# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-12-07 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skill_senpai', '0010_auto_20181206_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='LectureConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='preconditions',
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecture_id',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='lectureconnector',
            name='cur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current', to='skill_senpai.Lecture'),
        ),
        migrations.AddField(
            model_name='lectureconnector',
            name='pre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='previous', to='skill_senpai.Lecture'),
        ),
    ]
