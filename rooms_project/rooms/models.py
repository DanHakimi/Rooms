from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=255)

class Floor(models.Model):
    building = models.ForeignKey(Building, related_name="floors")
    name = models.CharField(
        max_length=100,
        help_text="For most buildings, the floors are just named by their number",
    )

class Room(models.Model):
    floor = models.ForeignKey(Floor, related_name="rooms")

    name = models.CharField(
        max_length=100,
        help_text="The name of the room, for many rooms this is just the number.",
    )