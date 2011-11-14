import datetime

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