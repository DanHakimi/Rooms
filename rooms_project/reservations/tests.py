import datetime

from django.core.urlresolvers import reverse

from rooms_project.cas_auth.models import CASUser
from rooms_project.rooms.models import Room, Floor, Building
from rooms_project.utils import BaseTestCase

from .models import ReservationRequest


class ReservationViewTest(BaseTestCase):
    def test_room_reservation_list(self):
        b = Building.objects.create(name="Test")
        f = b.floors.create(name="First")
        r = f.rooms.create(name="Room")

        self.get("api_v1_room_reservation_list", pk=1024, status_code=404)
        response = self.get("api_v1_room_reservation_list", pk=r.pk)
        self.assert_json_response(response, [])

        t = datetime.datetime.today()
        c = CASUser.objects.create(username="t1")
        rr = ReservationRequest.objects.create(
            status=ReservationRequest.UNREVIEWED,
            room=r,
            start_time=t,
            end_time=t,
            requester=c,
        )
        response = self.get("api_v1_room_reservation_list", pk=r.pk)
        self.assert_json_response(response, [])
        rr.status = ReservationRequest.ACCEPTED
        rr.save()
        response = self.get("api_v1_room_reservation_list", pk=r.pk)
        self.assert_json_response(response, [
            {
                "id": rr.id,
                "status": ReservationRequest.ACCEPTED,
                "room": r.to_json(),
                "start_time": t.isoformat(),
                "end_time": t.isoformat(),
                "requestor": {
                    "id": c.id,
                    "username": "t1",
                },
            }
        ])

    def test_reservation_request_create(self):
        url_name = "api_v1_room_reservation_request_create"

        b = Building.objects.create(name="Union")
        f = b.floors.create(name="Third")
        r = f.rooms.create(name="3606")

        response = self.get(url_name, pk=r.pk, status_code=302)
        self.assertEqual(response["Location"], "http://testserver" + reverse("auth_login"))

        user = CASUser.objects.create(username="gaynoa2")
        with self.login(user):
            self.post(url_name, pk=1024, status_code=404, data={})

            response = self.post(url_name, pk=r.pk, data={})
            self.assert_json_response(response, {
                "errors": {
                    "start_time": ["This field is required."],
                    "end_time": ["This field is required."],
                }
            })

            response = self.post(url_name, pk=r.pk, data={
                "start_time": "2011-11-15 13:40:00",
                "end_time": "2011-11-15 14:00:00",
            }, status_code=201)
            rr = ReservationRequest.objects.get()
            self.assert_json_response(response, {
                "id": rr.id,
                "room": r.to_json(),
                "status": ReservationRequest.UNREVIEWED,
                "requestor": user.to_json(),
                "start_time": "2011-11-15T13:40:00",
                "end_time": "2011-11-15T14:00:00",
            })
            self.assert_attrs(rr,
                requester=user,
                reviewer=None,
                start_time=datetime.datetime(2011, 11, 15, 13, 40),
                end_time=datetime.datetime(2011, 11, 15, 14),
            )

    def test_reservation_pending_list(self):
        url_name = "api_v1_room_reservation_pending_list"

        b = Building.objects.create(name="Union")
        f = b.floors.create(name="Third")
        r = f.rooms.create(name="3606")

        self.get(url_name, status_code=302)

        c = CASUser.objects.create(username="t1")
        t1 = datetime.datetime.today()
        t2 = datetime.datetime.today() + datetime.timedelta(days=1)
        rr1 = ReservationRequest.objects.create(
            status=ReservationRequest.UNREVIEWED,
            room=r,
            start_time=t1,
            end_time=t1,
            requester=c,
        )
        rr2 = ReservationRequest.objects.create(
            status=ReservationRequest.ACCEPTED,
            room=r,
            start_time=t2,
            end_time=t1,
            requester=c,
        )

        with self.login(c):
            self.get(url_name, status_code=302)

        admin = CASUser.objects.create(username="t2", is_admin=True)
        with self.login(admin):
            response = self.get(url_name)
            self.assert_json_response(response, [
                rr1.to_json()
            ])

    def test_reservation_accept_reject(self):
        accept_url_name = "api_v1_room_reservation_request_accept"
        reject_url_name = "api_v1_room_reservation_request_reject"

        b = Building.objects.create(name="Union")
        f = b.floors.create(name="Third")
        r = f.rooms.create(name="3606")


        c = CASUser.objects.create(username="t1")
        t = datetime.datetime.today()
        rr = ReservationRequest.objects.create(
            status=ReservationRequest.UNREVIEWED,
            room=r,
            start_time=t,
            end_time=t,
            requester=c,
        )
        self.get(accept_url_name, pk=rr.pk, status_code=302)
        self.get(reject_url_name, pk=rr.pk, status_code=302)
        with self.login(c):
            self.get(accept_url_name, pk=rr.pk, status_code=302)
            self.get(reject_url_name, pk=rr.pk, status_code=302)

        admin = CASUser.objects.create(username="t2", is_admin=True)
        with self.login(admin):
            response = self.get(reject_url_name, pk=rr.pk)
            rr = self.reload(rr)
            self.assert_json_response(response, rr.to_json())
            self.assert_attrs(rr, status=ReservationRequest.REJECTED)

            rr = ReservationRequest.objects.create(
                status=ReservationRequest.UNREVIEWED,
                room=r,
                start_time=t,
                end_time=t,
                requester=c,
            )
            response = self.get(accept_url_name, pk=rr.pk)
            rr = self.reload(rr)
            self.assert_json_response(response, rr.to_json())
            self.assert_attrs(rr, status=ReservationRequest.ACCEPTED)
