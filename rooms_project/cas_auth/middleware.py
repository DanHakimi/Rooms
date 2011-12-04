from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from .models import CASUser, UnauthenticatedUser
from .pycas import CAS


class CASMiddleware(object):
    def process_request(self, request):
        # TODO: move to a setting :(
        request.cas = CAS(
            base_url="https://cas-auth.rpi.edu/cas",
            service=request.build_absolute_uri("/"),
        )
        if "ticket" in request.GET:
            ticket = request.GET["ticket"]
            valid, info = request.cas.validate_ticket(ticket)
            if valid:
                request.user, _ = CASUser.objects.get_or_create(username=info["username"])
                request.session["cas:user"] = request.user.pk
            else:
                request.user = UnauthenticatedUser()
                try:
                    del request.session["cas:user"]
                except KeyError:
                    pass
            return redirect("home")
        elif "cas:user" in request.session:
            try:
                request.user = CASUser.objects.get(pk=request.session["cas:user"])
            except CASUser.DoesNotExist:
                del request.session["cas:user"]
                request.user = UnauthenticatedUser()
        else:
            request.user = UnauthenticatedUser()