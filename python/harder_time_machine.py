import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def time_machine(integer, string1):
  if string1 == 'hours':
      return starter + datetime.timedelta(hours=integer)
  elif string1 == 'days':
      return starter + datetime.timedelta(days=integer)
  elif string1 == 'minutes':
      return starter + datetime.timedelta(minutes=integer)
  elif string1 == 'years':
      return starter + datetime.timedelta(days=integer*365)

# You can't set "years" on a timedelta!

time_machine(3, 'days')