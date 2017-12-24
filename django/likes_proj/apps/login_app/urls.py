"""

APP LEVEL URLS
LOG IN APP

"""
from django.conf.urls import url
from . import views

def test(request):
    print """
        THIS IS MY TEST NUMBER 2
    """


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login)
    
]