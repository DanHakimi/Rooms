from django.shortcuts import get_object_or_404
from django.utils import simplejson as json

from rooms_project.utils import JSONResponse

from .models import Building


def building_list(request):
    return JSONResponse([
        b.to_json()
        for b in Building.objects.all()
    ])

def building_detail(request, pk):
    building = get_object_or_404(Building, pk=pk)
    return JSONResponse(building.to_json())

def floor_detail(request, building_pk, floor_pk):
    building = get_object_or_404(Building, pk=building_pk)
    floor = get_object_or_404(building.floors.all(), pk=floor_pk)
    return JSONResponse(floor.to_json())
