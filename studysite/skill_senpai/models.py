# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name


class Language(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name

class Lecture(models.Model):

	title = models.CharField(max_length=255, default='null')
	short_description = models.CharField(max_length=255, null=True)
	description = models.TextField(null=True)
	lecture_id = models.CharField(max_length=255, unique=True, null=True)
	categorie = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	credits = models.IntegerField(null=True)
	time = models.TimeField(null=True)
	nevents = models.IntegerField(null=True)
	tutorial = models.BooleanField(default=False)
   	languages = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):
		return 'Lecture: ' + self.title + " - " + self.lecture_id

class LectureConnector(models.Model):

	pre = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, related_name='previous')
	cur = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, related_name='current')

	def __unicode__(self):
		return 'Connector: Pre: ' + self.pre.lecture_id + ' -> Cur: ' + self.cur.lecture_id
