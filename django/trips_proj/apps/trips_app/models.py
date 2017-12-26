"""

APP LEVEL
TRIPS APP

"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User
from django.contrib import messages
import datetime
 
class TripsManager(models.Manager):
    def creator(self, postData):
        new_trip = self.create(destination = postData['destination'], description = postData['description'], start_date = postData['start_date'], end_date = postData['end_date'], planner = User.objects.get(id=id))
        return new_trip

def validator(self, postData):
        results = {'status': True, 'errors': []}
        if len(postData['destination']) < 3: #Checks how long the destination is.
            results['errors'].append('Trip destination must be at least 3 characters')
            results['status'] = False 
        if len(postData['description']) < 10: #Checks how long the decription is.
            results['errors'].append('Trip description must be longer')
            results['status'] = False
        if len(postData['start_date']) < 10:
            results['errors'].append('Date is not Valid')
            results['status'] = False              
        if len(postData['end_date']) < 10:
            results['errors'].append('Date is not valid')
            results['status'] = False  
        if datetime.datetime.now() > datetime.datetime.strptime(postData['start_date'].encode(), '%Y-%m-%d'):
            results['errors'].append('Trip Start Date must be after today')
            results['status'] = False  
        if postData['end_date'] < postData['start_Date']:
            results['errors'].append('Trip End Date must be after today')
            results['status'] = False  
        return results

	
	def group_trip(self, id, user_id):
		user_id = User.objects.get(id=user_id)
		trip_id = Trips.objects.get(id=id)
		trip_id.group_trip.add(user_id)

# Create your models here.
class Trips(models.Model):
	destination = models.CharField(max_length = 200)
	description = models.TextField()
	planner = models.ForeignKey(User, related_name="trips_planned")
	users = models.ManyToManyField(User, related_name="trips")
	start_date = models.DateField()
	end_date = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = TripsManager()