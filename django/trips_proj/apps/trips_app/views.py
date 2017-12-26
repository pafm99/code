"""

APP LEVEL
TRIPS APP

"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from ..login_app.models import User
from models import Trips
from django.contrib import messages


# Create your views here.

def dashboard(request):
    #print "TEST"
    #request.session.flush()
    curr_user = User.objects.get(id = request.session['id'], first_name = request.session['first_name'])
    #if curr_user in request.session:
        #curr_user = User.objects.get(id = request.session['id'], first_name = request.session['first_name'])
    context = {
        'my_trips': Trips.objects.filter(planner=curr_user).order_by('startDate'),
		'all_trips': Trips.objects.exclude(planner=curr_user).order_by('startDate'),
		#'joinedTrips': User.objects.get(id=curr_user).all()
    }
    return render(request, "trips_app/dashboard.html", context)
    """
    else:
        return redirect('/')
    """

def new(request):
    results = Trips.objects.validator(request.POST)
    if results['status'] == True:
        trip = Trips.objects.creator(request.POST)
        messages.success(request, "Trip was created")
    else:
        for error in results['errors']:
            messages.error(request, error)
    return redirect('/trips/')





  
def logout(request):
    request.session.flush()
    return redirect('/')
"""






#  *** REDIRECTS ***
def addTrip(request):
	if 'user' in request.session:
		if request.method == 'POST':		
			response = TripsDB.objects.createTrip(request.POST, request.session['user']['id'])
			if not response[0]:
				for message in response[1]:				
					messages.error(request, message[1])
				return redirect('trips:newTrip')
			else:
				# if response[0]:
				return redirect('trips:home')
		return redirect('trips:home')
	return redirect('logReg:index')

def join(request, id):
	if 'user' in request.session:
		TripsDB.objects.joinTrips(id, request.session['user']['id'])
		return redirect('trips:home')
	return redirect('logReg:index')
"""