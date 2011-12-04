from django import forms

from .models import ReservationRequest


class RoomReservationRequestForm(forms.ModelForm):
    class Meta:
        model = ReservationRequest
        fields = ["reason", "start_time", "end_time"]
        widgets = {
            "reason": forms.Textarea(attrs={"rows": 3, "class": "xxlarge"}),
        }

    def clean_end_time(self):
        start_time = self.cleaned_data.get("start_time")
        end_time = self.cleaned_data.get("end_time")
        if start_time and end_time and end_time <= start_time:
            raise forms.ValidationError("End time must be after start time.")
        return end_time