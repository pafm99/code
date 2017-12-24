from django.shortcuts import render, redirect
from models import User


def index(request):

    context = {
        'users': User.objects.all()
    }

    return render(request, 'surveys_apps/index.html', context)


def process(request):
    User.objects.create(name = request.POST['name'])
    return redirect('/')
