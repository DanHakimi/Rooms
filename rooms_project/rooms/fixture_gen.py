from fixture_generator import fixture_generator

from .models import Building, Floor, Room


@fixture_generator(Building, Floor, Room)
def rpi_union():
    union = Building.objects.create(name="The Union")
    union.floors.create(name="1st")
    union.floors.create(name="2nd")
    union.floors.create(name="3rd")