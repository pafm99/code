# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models

# Create your models here.
class Like(models.Model):
    giver = models.ForeignKey(User, related_name='gave')
    #user = User.obejcts.get(id = someid)
    #user.gave.all().count()
    receiver = models.ForeignKey(User, related_name="received")
    #user = User.obejcts.get(id = someid)
    #user.received.all().count()