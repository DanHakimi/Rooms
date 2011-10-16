from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import simplejson as json

from .models import Building


def building_list(request):
    response = HttpResponse(mimetype="application/json")
    json.dump([
        {"name": b.name, "id": b.pk}
        for b in Building.objects.all()
    ], response)
    return response

def building_detail(request, pk):
    building = get_object_or_404(Building, pk=pk)
    response = HttpResponse(mimetype="application/json")
    json.dump({
        "name": building.name,
        "id": building.pk,
        "floors": [
            {"id": f.pk, "name": f.name}
            for f in building.floors.all()
        ],
    }, response)
    return response

def floor_detail(request, building_pk, floor_pk):
    building = get_object_or_404(Building, pk=building_pk)
    floor = get_object_or_404(building.floors.all(), pk=floor_pk)
    response = HttpResponse(mimetype="application/json")
    json.dump({
        "name": floor.name,
        "id": floor.pk,
        "rooms": [
            {"id": r.pk, "name": r.name, "nickname": r.nickname, "capacity": r.capacity}
            for r in floor.rooms.all()
        ]
    }, response)
    return response