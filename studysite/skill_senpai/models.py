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

	title = models.CharField(max_length=255, null=True)
	description = models.TextField(null=True)
	lecture_id = models.CharField(max_length=255, null=True)
   	preconditions = models.ManyToManyField("self", blank=True)
	categorie = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	credits = models.IntegerField(null=True)
	time = models.TimeField(null=True)
	nevents = models.IntegerField(null=True)
	tutorial = models.BooleanField(default=False)
   	languages = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):
		return 'Lecture: ' + self.title + " - " + self.lecture_id

