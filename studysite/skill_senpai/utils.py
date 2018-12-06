# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from skill_senpai.models import Lecture


def get_lecture(skills):
	Lecture.objects.none()

	return_list = []

	# nicu desu
	for item in skills:
		return_list.append(Lecture.objects.get(lecture_id=item))

	return return_list


def get_preconditions():
	pass
