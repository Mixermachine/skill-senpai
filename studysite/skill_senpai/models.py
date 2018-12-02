# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Subject(models.Model):
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
