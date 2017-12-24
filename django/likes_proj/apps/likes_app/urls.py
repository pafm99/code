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
    url(r'^$', views.dashboard),
    url(r'^give/(?P<id>\d+)$', views.give),
    
]