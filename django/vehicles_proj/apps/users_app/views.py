# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'users_app/index.html')

def register(request):
    results = User.objects.validate(request.POST)
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        messages.success(request, "User was created")
    else:
        for error in results['errors']:
            messages.error(request, error)
    return redirect('/')

def login(request):
    #print "I am in log in"
    results = User.objects.logVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    request.session['email'] = results['user'].email
    request.session['first_name'] = results['user'].first_name
    return redirect('/dashboard')

