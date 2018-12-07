# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from skill_senpai.models import Lecture


def get_lecture(skills):
	Lecture.objects.none()

	return_list = []

	# nicu desu
	for id in skills:
		get_preconditions_rec(return_list, id)

	ret_dict = {}
	ret_dict['lectures'] = return_list
	return ret_dict


def get_preconditions_rec(list, id): # might send duplicate title, can be improved
	database_item = Lecture.objects.get(lecture_id=id)
	if database_item.preconditions:
		for precondition in database_item.preconditions:
			lecture = {'lecture_id': database_item.lecture_id, 'title': database_item.title,
					   'precondition': precondition}
		list.append(lecture)
		get_preconditions_rec(list, precondition)
	else:
		list.append({'lecture_id': database_item.lecture_id, 'title': database_item.title, 'precondition': ""})
	pass
