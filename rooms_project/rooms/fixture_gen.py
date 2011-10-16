from fixture_generator import fixture_generator

from .models import Building, Floor, Room


@fixture_generator(Building, Floor, Room)
def rpi_union():
    union = Building.objects.create(name="The Union")

    first = union.floors.create(name="1st")
    second = union.floors.create(name="2nd")
    third = union.floors.create(name="3rd")

    third.rooms.create(
        name="3606",
        nickname="Shellnut Gallery",
        capacity=40,
    )