# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from skill_senpai import models

# Register your models here.

admin.site.register(models.Lecture)
admin.site.register(models.Category)
admin.site.register(models.Language)