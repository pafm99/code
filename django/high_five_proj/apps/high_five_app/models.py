# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
from ..login_app.models import User
from datetime import datetime

# Create your models here.
class HighFive(models.Model):
    gave = models.ForeignKey(User,related_name="giver")
    received = models.ForeignKey(User,related_name="receiver")
    created_at = models.DateTimeField(auto_now_add=True)