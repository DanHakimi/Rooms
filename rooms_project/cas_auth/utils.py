import functools

from django.shortcuts import redirect


def login_required(view):
    @functools.wraps(view)
    def inner(request, *args, **kwargs):
        if not request.user:
            return redirect("auth_login")
        return view(request, *args, **kwargs)
    return inner

def admin_required(view):
    @functools.wraps(view)
    def inner(request, *args, **kwargs):
        if not request.user or not request.user.is_admin:
            return redirect("auth_login")
        return view(request, *args, **kwargs)
    return inner