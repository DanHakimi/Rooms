from django.shortcuts import get_object_or_404, render

from rooms_project.utils import JSONResponse

from .models import Building, Room

# HTML VIEWS

def building_list(request):
    return render(request, "rooms/building_list.html", {
        "buildings": Building.objects.all(),
    })

def building_detail(request, pk):
    building = get_object_or_404(Building, pk=pk)
    return render(request, "rooms/building_detail.html", {
        "building": building,
    })

def room_detail(request, building_pk, room_pk):
    room = get_object_or_404(Room, pk=room_pk, floor__building__pk=building_pk)
    return render(request, "rooms/room_detail.html", {
        "room": room,
    })

# API VIEWS

def api_building_list(request):
    return JSONResponse([
        b.to_json()
        for b in Building.objects.all()
    ])

def api_building_detail(request, pk):
    building = get_object_or_404(Building, pk=pk)
    return JSONResponse(building.to_json())

def api_floor_detail(request, building_pk, floor_pk):
    building = get_object_or_404(Building, pk=building_pk)
    floor = get_object_or_404(building.floors.all(), pk=floor_pk)
    return JSONResponse(floor.to_json())
