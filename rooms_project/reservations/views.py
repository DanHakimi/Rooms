from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from rooms_project.cas_auth.utils import login_required, admin_required
from rooms_project.rooms.models import Room
from rooms_project.utils import JSONResponse

from .forms import RoomReservationRequestForm
from .models import ReservationRequest



def room_reservation_list(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return JSONResponse([
        reservation.to_json()
        for reservation in room.reservation_requests.filter(status=ReservationRequest.ACCEPTED)
    ])

@login_required
@require_POST
def room_reservation_request_create(request, pk):
    room = get_object_or_404(Room, pk=pk)
    form = RoomReservationRequestForm(request.POST)
    if form.is_valid():
        rr = form.save(commit=False)
        rr.requester = request.user
        rr.room = room
        rr.save()
        response = JSONResponse(rr.to_json(), status_code=201)
        response["Location"] = reverse("api_v1_room_reservation_list", kwargs={"pk": room.pk})
        return response
    else:
        return JSONResponse({"errors": form.errors})

@admin_required
def room_reservation_pending_list(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return JSONResponse([
        room.to_json()
        for room in room.reservation_requests.filter(status=ReservationRequest.UNREVIEWED)
    ])