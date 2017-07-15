# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from .models import VacantLocation 

from django.template import loader
# Create your views here.
# EXAMPLES
# polls/views.py
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
# # 
# from django.http import HttpResponse
# from django.template import loader

# from .models import Question


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


def index(request):
	vacant_locations = VacantLocation.objects.order_by()
	template = loader.get_template('vacant_dc2/index.html')
	context = { 
	'vacant_locations': vacant_locations,
	 }
	return HttpResponse(template.render(context, request))