from django.db import models

from rooms_project.cas_auth.models import CASUser
from rooms_project.rooms.models import Room


class ReservationRequest(models.Model):
    UNREVIEWED = 0
    ACCEPTED = 1
    REJECTED = 2

    STATUS_CHOICES = [
        (UNREVIEWED, "submitted, but not reviewed"),
        (ACCEPTED, "accepted"),
        (REJECTED, "rejected"),
    ]

    status = models.IntegerField(choices=STATUS_CHOICES, default=UNREVIEWED)
    room = models.ForeignKey(Room)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    requester = models.ForeignKey(CASUser)
