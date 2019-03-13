# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class SkillSenpaiConfig(AppConfig):
    name = 'skill_senpai'

    def ready(self):
        import skill_senpai.signals