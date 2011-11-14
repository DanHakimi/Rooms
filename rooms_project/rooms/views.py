from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import simplejson as json

from .models import Building


def building_list(request):
    response = HttpResponse(mimetype="application/json")
    json.dump([
        b.to_json()
        for b in Building.objects.all()
    ], response)
    return response

def building_detail(request, pk):
    building = get_object_or_404(Building, pk=pk)
    response = HttpResponse(mimetype="application/json")
    json.dump(building.to_json(), response)
    return response

def floor_detail(request, building_pk, floor_pk):
    building = get_object_or_404(Building, pk=building_pk)
    floor = get_object_or_404(building.floors.all(), pk=floor_pk)
    response = HttpResponse(mimetype="application/json")
    json.dump(floor.to_json(), response)
    return response