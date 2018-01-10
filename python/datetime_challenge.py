# naive is a datetime with no timezone.
# Create a new timezone for US/Pacific, which is 8 hours behind UTC (UTC-08:00).
# Then make a new variable named hill_valley that is naive with its tzinfo attribute replaced with the US/Pacific timezone you made.


import datetime

naive = datetime.datetime(2015, 10, 21, 4, 29)
usPacific = datetime.timezone(datetime.timedelta(hours=-8))

hill_valley = datetime.datetime(2014,4,21,9, tzinfo=usPacific)