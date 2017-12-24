"""

APP LEVEL URLS
HIGH FIVE APP

"""
from django.conf.urls import url
from . import views

def test(request):
    print """
        THIS IS MY TEST NUMBER 2
    """


urlpatterns = [
    #url(r'^$', views.index),
    #url(r'^register$', views.register),
    url(r'^give/(?P<id>\d+)$', views.give),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout)
    
]