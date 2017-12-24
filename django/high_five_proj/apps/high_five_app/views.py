# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import HighFive
from ..login_app.models import User


# Create your views here.

def dashboard(request):
    #high_five = HighFive.objects.filter(gave=User.objects.get(id=id))
    user = User.objects.get(id=request.session['id'])
    context = {
        'curr_user': User.objects.get(id=request.session['id']),
        'other': User.objects.exclude(id=request.session['id']),
        'count': None,
    }
    
    context['count'] = HighFive.objects.filter(received=User.objects.get(id=request.session['id']))
    return render(request, 'high_five_app/dashboard.html', context)

def give(request):
    card =Card.objects.get(id=id)
    user = User.objects.get(id=request.session['id'])
    user.cards.add(card)
    return redirect('/cards/')


def logout(request):
    request.session.flush()
    return redirect('/')