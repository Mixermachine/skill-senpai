# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.template import Context, loader
from django.utils import timezone
from utils import get_lecture

from models import Lecture

import json


def index(request):
    return HttpResponse(loader.get_template('index.html').render())

def query_lectures(request):
	# json object to return
	if request.method == 'POST':

		received_json_data = json.loads(request.body)

		return JsonResponse(get_lecture(received_json_data))

	return HttpResponse(status=404)

class LectureDetailView(DetailView):

	model = Lecture
	template_name = 'lecture_detail.html'

	def get_context_data(self, **kwargs):

		context = super(LectureDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()


		return context