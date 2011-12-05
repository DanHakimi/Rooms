from django.conf.urls.defaults import patterns, url, include

from . import views


urlpatterns = patterns("",
    url(r"^reservations/$", views.room_reservation_request_list_current, name="room_reservation_request_list_current"),
    url(r"^reservations/room/(?P<pk>\d+)/create/$", views.room_reservation_request_create, name="room_reservation_request_create"),
    url(r"^reservations/pending/$", views.room_reservation_pending_list, name="room_reservation_pending_list"),
    url(r"^reservations/(?P<pk>\d+)/accept/$", views.room_reservation_request_accept, name="room_reservation_request_accept"),
    url(r"^reservations/(?P<pk>\d+)/reject/$", views.room_reservation_request_reject, name="room_reservation_request_reject"),
    url(r"^api/v1/", include(patterns("",
        url(r"^reservations/room/(?P<pk>\d+)/$", views.api_room_reservation_list, name="api_v1_room_reservation_list"),
        url(r"^reservations/room/(?P<pk>\d+)/create/$", views.api_room_reservation_request_create, name="api_v1_room_reservation_request_create"),
        url(r"^reservations/(?P<pk>\d+)/accept/$", views.api_room_reservation_request_accept, name="api_v1_room_reservation_request_accept"),
        url(r"^reservations/(?P<pk>\d+)/reject/$", views.api_room_reservation_request_reject, name="api_v1_room_reservation_request_reject"),
        url(r"^reservations/pending/$", views.api_room_reservation_pending_list, name="api_v1_room_reservation_pending_list"),
    ))),
)