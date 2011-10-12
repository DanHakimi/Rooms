from django.http import HttpResponse
from django.utils import simplejson as json

from .models import Building


def building_list(request):
    response = HttpResponse(mimetype="application/json")
    json.dump([
        {"name": b.name, "id": b.pk}
        for b in Building.objects.all()
    ], response)
    return response