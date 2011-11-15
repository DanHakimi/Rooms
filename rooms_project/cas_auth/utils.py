import functools

from django.shortcuts import redirect


def login_required(view):
    @functools.wraps(view)
    def inner(request, *args, **kwargs):
        if request.user is None:
            return redirect("auth_login")
        return view(request, *args, **kwargs)
    return inner