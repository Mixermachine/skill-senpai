# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.template import Context, loader
from utils import get_lecture

import json


def index(request):
    return HttpResponse(loader.get_template('index.html').render())

def query_lectures(request):
	# json object to return
	if request.method == 'POST':

		received_json_data = json.loads(request.body)

		return JsonResponse(get_lecture(received_json_data))

	return HttpResponse(status=404)
