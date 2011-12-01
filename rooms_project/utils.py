import contextlib

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.test import TestCase
from django.utils import simplejson as json
from django.utils.importlib import import_module


class BaseTestCase(TestCase):
    def get(self, url_name, *args, **kwargs):
        status_code = kwargs.pop("status_code", 200)
        response = self.client.get(reverse(url_name, args=args, kwargs=kwargs))
        self.assertEqual(response.status_code, status_code)
        return response

    def post(self, url_name, *args, **kwargs):
        status_code = kwargs.pop("status_code", 200)
        data = kwargs.pop("data")
        response = self.client.post(reverse(url_name, args=args, kwargs=kwargs), data=data)
        self.assertEqual(response.status_code, status_code)
        return response

    def reload(self, obj):
        return obj.__class__._default_manager.get(pk=obj.pk)

    @contextlib.contextmanager
    def login(self, user):
        # Copied from TestCase.login
        engine = import_module(settings.SESSION_ENGINE)
        if self.client.session:
            session = self.client.session
        else:
            session = engine.SessionStore()
        session["cas:user"] = user.pk
        session.save()
        session_cookie = settings.SESSION_COOKIE_NAME
        self.client.cookies[session_cookie] = session.session_key
        cookie_data = {
            "max-age": None,
            "path": "/",
            "domain": settings.SESSION_COOKIE_DOMAIN,
            "secure": settings.SESSION_COOKIE_SECURE or None,
            "expires": None,
        }
        self.client.cookies[session_cookie].update(cookie_data)
        try:
            yield
        finally:
            del session["cas:user"]
            del self.client.cookies[session_cookie]
            session.save()

    def assert_json_response(self, response, data):
        self.assertEqual(json.loads(response.content), data)

    def assert_attrs(self, obj, **kwargs):
        for attr, expected_value in kwargs.iteritems():
            self.assertEqual(getattr(obj, attr), expected_value)

def JSONResponse(obj, status_code=200):
    response = HttpResponse(mimetype="application/json", status=status_code)
    json.dump(obj, response)
    return response