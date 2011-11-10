"""
Originally copyright Noah Kantrowitz, used under the terms of the BSD license.
"""
import contextlib
import urllib
import urllib2


class CAS(object):
    def __init__(self, base_url, service, login_path="/login",
                 logout_path="/logout", validate_path="/validate"):

        self.base_url = base_url
        self.service = service
        self.login_path = login_path
        self.logout_path = logout_path
        self.validate_path = validate_path

    def get_login_url(self):
        return "%s%s?service=%s" % (
            self.base_url, self.login_path, urllib.quote_plus(self.service)
        )

    def get_logout_url(self):
        return "%s%s?url=%s" % (
            self.base_url, self.logout_path, urllib.quote_plus(self.service)
        )

    def get_validate_url(self, ticket):
        return "%s%s?service=%s&ticket=%s" % (
            self.base_url, self.validate_path, urllib.quote_plus(self.service), urllib.quote_plus(ticket)
        )

    def validate_ticket(self, ticket):
        url = self.get_validate_url(ticket)
        with contextlib.closing(urllib2.urlopen(url)) as f:
            content = f.readlines()
        valid = content[0].strip() == "yes"
        info = {}
        if valid:
            info["username"] = content[1].strip()
        return valid, info
