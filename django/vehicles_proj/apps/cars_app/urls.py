from django.conf.urls import url
from . import views

def test(request):
    print "Lets TestHHHHHJHJHJHJHJHHJH"


urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add)
]
