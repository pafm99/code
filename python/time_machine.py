# Write a function named delorean that takes an integer. Return a datetime that is that many hours ahead from starter.


import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def delorean(integer):
  return starter + datetime.timedelta(hours=integer)