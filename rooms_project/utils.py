from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.test import TestCase
from django.utils import simplejson as json


class BaseTestCase(TestCase):
    def get(self, url_name, *args, **kwargs):
        status_code = kwargs.pop("status_code", 200)
        response = self.client.get(reverse(url_name, args=args, kwargs=kwargs))
        self.assertEqual(response.status_code, status_code)
        return response

    def assert_json_response(self, response, data):
        self.assertEqual(json.loads(response.content), data)

def JSONResponse(obj):
    response = HttpResponse(mimetype="application/json")
    json.dump(obj, response)
    return response