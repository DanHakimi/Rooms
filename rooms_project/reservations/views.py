from django.shortcuts import get_object_or_404

from rooms_project.rooms.models import Room
from rooms_project.utils import JSONResponse

from .models import ReservationRequest



def room_reservation_list(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return JSONResponse([
        reservation.to_json()
        for reservation in room.reservation_requests.filter(status=ReservationRequest.ACCEPTED)
    ])
