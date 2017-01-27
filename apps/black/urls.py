from django.conf.urls import url
from . import views
  # def method_to_run(request):
  #     print "Whatever route that was hit by an HTTP request (by the way) decided to invoke me!"
  #     print "By the way, here's the request object that Django automatically passes us:", request
  #     print "By the by, we still aren't delivering anything to the browser, so you should see 'ValueError at /'"
urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^wishlist$', views.wishlist, name = 'wishlist'),
    url(r'^black/display/(?P<id>\d+)$', views.display, name = 'display'),
    url(r'^home$', views.home, name = 'home'),
    url(r'^add$', views.add, name = 'add'),
    url(r'^addItem$', views.addItem, name = 'addItem'),
    url(r'^remove$', views.remove, name = 'remove'),
    url(r'^black/delete/(?P<id>\d+)$', views.delete, name = 'delete'),


 ]
