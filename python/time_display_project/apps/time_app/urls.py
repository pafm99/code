from django.conf.urls import url
from . import views

def test(request):
    print "test its working too"

urlpatterns = [
    url(r'^$', views.index),

]
