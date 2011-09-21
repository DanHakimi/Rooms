from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns("",
    url(r"^login/$", views.login, name="auth_login"),
    url(r"^logout/$", views.logout, name="auth_logout"),
)