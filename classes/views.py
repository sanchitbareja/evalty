from django.template import Context, RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.loader import render_to_string
from django import forms
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
import os, time, simplejson
from datetime import datetime, timedelta, time
from django.http import Http404


def home(request):
    """Home view"""
    return render_to_response('splash.html', {}, RequestContext(request))

def student(request):
    """Student view"""
    return render_to_response('student.html', {'student':True}, RequestContext(request))

def student_evaluation_select_team(request):
    """Student submitting a new evaluation view"""
    return render_to_response('student_evaluation_select_team.html', {'student':True}, RequestContext(request))

def student_evaluation_form(request):
    """Student submitting a new evaluation view"""
    return render_to_response('student_evaluation.html', {'student':True}, RequestContext(request))

def student_evaluation_report(request):
    """Student submitting a new evaluation view"""
    return render_to_response('student_evaluation_report.html', {'student':True}, RequestContext(request))

def professor(request):
    """Professor view"""
    return render_to_response('professor.html', {'professor':True}, RequestContext(request))

def professor_evaluation_report(request):
    """Professor view"""
    return render_to_response('professor_evaluation_report.html', {'professor':True}, RequestContext(request))
