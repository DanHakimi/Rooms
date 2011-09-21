from django.shortcuts import redirect


def login(request):
    return redirect(request.cas.get_login_url())

def logout(request):
    try:
        del request.session["cas:user"]
    except KeyError:
        pass
    return redirect(request.cas.get_logout_url())