# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

# Create your models here.

class UserManager(models.Manager):
    def creator(self, postData):
        user = self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))

    def validate(self, postData):
        results = {'status': True, 'errors': []}
        if len(postData['first_name']) < 3:
            results['errors'].append('Your First name is too god damn short fool')
            results['status'] = False
        if ' ' in postData['first_name']:
            results['errors'].append('Your First Name cannot have spaces')
            results['status'] = False 
        if len(postData['last_name']) < 3:
            results['errors'].append('Your Last name is too god damn short fool')
            results['status'] = False
        if ' ' in postData['last_name']:
            results['errors'].append('Your Last Name cannot have spaces')
            results['status'] = False   
        if len(postData['email']) < 3:
            results['errors'].append('Your email is too god damn short fool')
            results['status'] = False
        if ' ' in postData['email']:
            results['errors'].append('Your email cannot have spaces')
            results['status'] = False       
        if len(postData['password']) < 3:
            results['errors'].append('Your Password is too god damn short fool')
            results['status'] = False 
        if len(postData['password']) > 15:
            results['errors'].append('Your password is too long')
            results['status'] = False
        if ' ' in postData['password']:
            results['errors'].append('Your email cannot have spaces')
            results['status'] = False               
        if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
            results['errors'].append('Your email is not valid fool')
            results['status'] = False                  
        if len(self.filter(email = postData['email'])) > 0:
            results['errors'].append('User already exists')
            results['status'] = False
        if postData['password'] != postData['c_password']:
            results['errors'].append('Your Passwords Do not match')
            results['status'] = False

        return results
    def logVal(self, postData):
        results = {
            "status": True,
            "errors": [],
            "users": None
        }
        users = self.filter(email = postData['email'])
        if len(users) < 1:
            results['errors'].append('You are not registered')
        else:
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()) == False:
                results['errors'].append('Password is incorrect. Please try again')
            if len(results['errors']) > 0:
                results['status'] = False
            else:
                results['user'] = users[0]
            return results



class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField(default=2000)
    user = models.ForeignKey(User, related_name="cars")


