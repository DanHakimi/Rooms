from rooms_project.utils import BaseTestCase

from .models import Building


class RoomViewTests(BaseTestCase):
    def test_building_list_api(self):
        b = Building.objects.create(name="Blitman Hall")
        q = Building.objects.create(name="Quad")

        response = self.get("api_v1_building_list")
        self.assert_json_response(response, [
            {
                "name": "Blitman Hall",
                "id": b.pk,
                "floors": [],
            },
            {
                "name": "Quad",
                "id": q.pk,
                "floors": [],
            }
        ])

    def test_building_detail_api(self):
        self.get("api_v1_building_detail", pk=2345, status_code=404)

        b = Building.objects.create(name="Blitman Hall")
        [f1, f2, f3, f4] = [
            b.floors.create(name=name)
            for name in ["First", "Second", "Third", "Fourth"]
        ]

        response = self.get("api_v1_building_detail", pk=b.pk)
        self.assert_json_response(response, {
            "name": "Blitman Hall",
            "id": b.pk,
            "floors": [
                {
                    "name": "First",
                    "id": f1.pk,
                    "rooms": [],
                },
                {
                    "name": "Second",
                    "id": f2.pk,
                    "rooms": [],
                },
                {
                    "name": "Third",
                    "id": f3.pk,
                    "rooms": [],
                },
                {
                    "name": "Fourth",
                    "id": f4.pk,
                    "rooms": [],
                },
            ],
        })

    def test_floor_detail(self):
        self.get("api_v1_floor_detail", building_pk=12, floor_pk=3, status_code=404)

        b = Building.objects.create(name="The Union")
        self.get("api_v1_floor_detail", building_pk=b.pk, floor_pk=12, status_code=404)

        floor = b.floors.create(name="Third Floor")
        room = floor.rooms.create(
            name="3606",
            nickname="Shellnut Gallery",
        )

        response = self.get("api_v1_floor_detail", building_pk=b.pk, floor_pk=floor.pk)
        self.assert_json_response(response, {
            "name": "Third Floor",
            "id": floor.pk,
            "rooms": [
                {
                    "id": room.pk,
                    "name": "3606",
                    "nickname": "Shellnut Gallery",
                    "capacity": None,
                    "description": "",
                }
            ],
        })