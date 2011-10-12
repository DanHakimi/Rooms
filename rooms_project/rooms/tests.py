from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import simplejson as json

from .models import Building


class RoomViewTests(TestCase):
    def get(self, url_name, *args, **kwargs):
        return self.client.get(reverse(url_name, args=args, kwargs=kwargs))

    def test_building_list_api(self):
        b = Building.objects.create(name="Blitman Hall")
        q = Building.objects.create(name="Quad")

        response = self.get("api_v1_building_list")
        self.assertEqual(json.loads(response.content), [
            {
                "name": "Blitman Hall",
                "id": b.pk,
            },
            {
                "name": "Quad",
                "id": q.pk,
            }
        ])