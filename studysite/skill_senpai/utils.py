# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from skill_senpai.models import Lecture
from skill_senpai.models import LectureConnector


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
	try:
		database_item = Lecture.objects.get(lecture_id=id)
	except:
		# dirty
		list = []
		list.append({'error': id})
		return
	item_connectors = LectureConnector.objects.filter(cur=database_item).all()
	if item_connectors:
		for connector in item_connectors:
			lecture = {'lecture_id': database_item.lecture_id, 'title': database_item.title, 'precondition': connector.pre.lecture_id, 'importance': connector.importance}
			if not check_if_precondition_duplicate(list, lecture):
				list.append(lecture)
				get_preconditions_rec(list, connector.pre.lecture_id)
			else:
				print "Warning found loop " + lecture['lecture_id'] + " <-> " + lecture['precondition']
	else:
		list.append({'lecture_id': database_item.lecture_id, 'title': database_item.title, 'precondition': ""})
	pass


def check_if_precondition_duplicate(list, lecture):
	for item in list:
		if item['lecture_id'] == lecture['lecture_id'] and item['precondition'] == lecture['precondition']:
			return True
	return False

def get_number_of_lectures():
	return Lecture.objects.all().count()