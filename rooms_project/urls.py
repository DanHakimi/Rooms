from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import render_to_response
from django.template import RequestContext

from . import views


urlpatterns = patterns('',
    url(r"^$", views.home, name="home"),
    url(r"^user/", include("rooms_project.cas_auth.urls")),
    url(r"", include("rooms_project.rooms.urls")),
    url(r"", include("rooms_project.reservations.urls")),
) + staticfiles_urlpatterns()
