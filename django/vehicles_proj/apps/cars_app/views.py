# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..users_app.models import Car, User
from django.shortcuts import render

# Create your views here.
def index(request):
    context ={
        "user" : request.session['first_name'],
    }
    return render(request, "cars_app/dashboard.html", context)

def add(request):
    

