from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import simplejson as json

from .models import Building


class RoomViewTests(TestCase):
    def get(self, url_name, *args, **kwargs):
        status_code = kwargs.pop("status_code", 200)
        response = self.client.get(reverse(url_name, args=args, kwargs=kwargs))
        self.assertEqual(response.status_code, status_code)
        return response

    def test_building_list_api(self):
        b = Building.objects.create(name="Blitman Hall")
        q = Building.objects.create(name="Quad")

        response = self.get("api_v1_building_list")
        self.assertEqual(json.loads(response.content), [
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
        self.assertEqual(json.loads(response.content), {
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
        self.assertEqual(json.loads(response.content), {
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