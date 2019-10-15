from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shows$', views.index),
    url(r'^shows/(?P<show_id>\d+)$', views.show_profile),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit_show),
    url(r'^shows/new$', views.new_show),
    url(r'^shows/create$', views.add_show_from_form),
    url(r'^shows/(?P<show_id>\d+)/update$', views.update_show),
    url(r'^shows/(?P<show_id>\d+)/destroy$', views.delete_show),
]