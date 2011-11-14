from django.conf.urls.defaults import patterns, url, include

from . import views


urlpatterns = patterns("",
    url(r"^api/v1/", include(patterns("",
        url(r"^reservations/room/(?P<pk>\d+)/$", views.room_reservation_list, name="api_v1_room_reservation_list"),
    ))),
)