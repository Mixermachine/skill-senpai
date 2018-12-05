# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

import json


def index(request):
    return HttpResponse("Hello, world. You're at the skill_senpais index.")


def query_lectures(request):

	# json object to return
	data

	if request.method=='POST':

		received_json_data=json.loads(request.POST['data'])
		# fill json response here
		data = {'foo': 'bar', 'hello': 'world'}

	return HttpResponse(json.dumps(data), content_type='application/json')



class IndexView(TemplateView):
    template_name = "about.html"