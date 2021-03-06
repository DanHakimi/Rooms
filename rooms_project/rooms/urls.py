from django.conf.urls.defaults import patterns, url, include

from . import views


urlpatterns = patterns("",
    url(r"^building/$", views.building_list, name="building_list"),
    url(r"^building/(?P<pk>\d+)/$", views.building_detail, name="building_detail"),
    url(r"^building/(?P<building_pk>\d+)/room/(?P<room_pk>\d+)/$", views.room_detail, name="room_detail"),
    url(r"^api/v1/", include(patterns("",
        url(r"^building/$", views.api_building_list, name="api_v1_building_list"),
        url(r"^building/(?P<pk>\d+)/$", views.api_building_detail, name="api_v1_building_detail"),
        url(r"^building/(?P<building_pk>\d+)/floor/(?P<floor_pk>\d+)/$", views.api_floor_detail, name="api_v1_floor_detail"),
    ))),
)