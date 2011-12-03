from django import forms

from .models import ReservationRequest


class RoomReservationRequestForm(forms.ModelForm):
    class Meta:
        model = ReservationRequest
        fields = ["reason", "start_time", "end_time"]
        widgets = {
            "reason": forms.Textarea(attrs={"rows": 3, "class": "xxlarge"}),
        }