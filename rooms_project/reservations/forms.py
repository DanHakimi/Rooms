from django import forms

from .models import ReservationRequest


class RoomReservationRequestForm(forms.ModelForm):
    class Meta:
        model = ReservationRequest
        fields = ["start_time", "end_time"]