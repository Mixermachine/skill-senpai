# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from utils import get_lecture

import json


def index(request):
    return HttpResponse("Hello, world. You're at the skill_senpais index.")


def query_lectures(request):
#	from pudb import set_trace
#	set_trace()
	# json object to return
	if request.method=='POST':

		received_json_data=json.loads(request.body)

		return JsonResponse(get_lecture(received_json_data))

	return HttpResponse(status=404)




class IndexView(TemplateView):
    template_name = "about.html"