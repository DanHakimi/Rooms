from fixture_generator import fixture_generator

from .models import Building, Floor, Room

@fixture_generator(Building, Floor, Room)
def rpi_union():
    union = Building.objects.create(name="The Union")
    first_floor = union.floors.create(name="1st")
    second_floor = union.floors.create(name="2nd")
    third_floor = union.floors.create(name="3rd")
		first_floor.rooms.create(capacity=100, name="Some Room", nickname="cool room")
		