from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=255)

class Floor(models.Model):
    building = models.ForeignKey(Building, related_name="floors")
    name = models.CharField(
        max_length=100,
        help_text="For most buildings, the floors are just named by their number",
    )
    map_img = models.ImageField(upload_to="maps/")

class Room(models.Model):
    floor = models.ForeignKey(Floor, related_name="rooms")

    name = models.CharField(
        max_length=100,
        help_text="The name of the room, for many rooms this is just the number.",
    )
    nickname = models.CharField(
        max_length=255,
        help_text="Optional nickname field, e.g. Union 3606 is Shellnut Gallary"
    )
    description = models.TextField()
    image = models.ImageField(upload_to="rooms/")

    capacity = models.IntegerField(
        null=True, blank=True,
        help_text="Number of people the room can hold."
    )