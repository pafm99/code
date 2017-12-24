from django.conf.urls import url
from . import views



def test(request):
    print "Here I am again"

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process)
]
