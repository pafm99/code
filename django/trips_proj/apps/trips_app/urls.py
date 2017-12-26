from django.conf.urls import url
from . import views

def test(request):
    print "Testing 2"

urlpatterns = [
    url(r'^dashboard/', views.dashboard),
    url(r'^new/', views.new),
    #url(r'^view/(?P<id>\d+)$', views.view),
    #url(r'^remove/(?P<id>\d+)$', views.remove),
    #url(r'^logout$', views.remove)
]