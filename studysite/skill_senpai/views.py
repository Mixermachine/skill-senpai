# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.detail import DetailView

from models import Lecture
from utils import get_lecture


def simpleProcessor(request):
	if request.path == '/':
		return HttpResponse(loader.get_template('index.html').render())
	else:
		return HttpResponse(loader.get_template(request.path.replace('/', '') + '.html').render())


@csrf_exempt
def query_lectures(request):
	# json object to return
	if request.method == 'POST':

		received_json_data = json.loads(request.body)

		return JsonResponse(get_lecture(received_json_data))

	return HttpResponse(status=404)


class LectureDetailView(DetailView):
	model = Lecture
	template_name = 'lecture_detail.html'

	def get_object(self):
		return get_object_or_404(Lecture, lecture_id=self.kwargs['lecture_id'])

	def get_context_data(self, **kwargs):

		context = super(LectureDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context
