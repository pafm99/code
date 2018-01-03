# Write a function named time_tango that takes a date and a time. It should combine them into a datetime and return it.


import datetime 

def time_tango(date, time):
    return datetime.datetime.combine(date, time)