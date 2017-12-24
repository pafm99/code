# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User
from models import Like

# Create your views here.
def dashboard(request):
    context = {
        'otherusers': User.objects.exclude(id=request.session['id']),
        'curr_user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'likes_app/dashboard.html')

def give(request, id):
    Like.objects.create(giver = User.objects.get(id=request.session['id']),
    receiver = User.objects.get(id=id))
    return redirect('/like/')
