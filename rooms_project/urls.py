from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import render_to_response
from django.template import RequestContext


def static_view(request, path):
    """
    serve pages directly from the templates directories.
    """
    if not path or path.endswith("/"):
        template_name = path + "index.html"
    else:
        template_name = path
    ctx = RequestContext(request)
    return render_to_response(template_name, ctx)

urlpatterns = staticfiles_urlpatterns() + patterns('',
    url(r"^user/", include("rooms_project.cas_auth.urls")),
   // url(r"^docs", ),
    url(r"^(?P<path>.*)$", static_view),
)
