from fixture_generator import fixture_generator

from .models import Building, Floor, Room

@fixture_generator(Building, Floor, Room)
def rpi_union():
    union = Building.objects.create(name="The Union")

    first = union.floors.create(name="1st")
    second = union.floors.create(name="2nd")
    third = union.floors.create(name="3rd")

    third.rooms.create(
        name="3202",
        capacity=40,
        description="Used for formal and informal meetings with groups of 40 or less and is equipped with tables, chairs, and pull down screen.  There are six network jacks, access to the food elevator and patio, and TV hookup.\nDimensions: 22' 3\" X 38' 3\""
    )
    third.rooms.create(
        name="3502",
        capacity=20,
        description="Used for formal and informal meetings with groups of 20 or less and is equipped with tables, chairs, overhead, and pull down screen.  There are four network jacks and TV hookup."
    )
    third.rooms.create(
        name="3510",
        capacity=15,
        description="Used for formal and informal meetings with groups of 15 or less and is equipped with tables, chairs.  There are six network jacks."
    )
    third.rooms.create(
        name="3511",
        capacity=20,
        description="Used for formal and informal meetings with groups of 20 or less and is equipped with tables, chairs, and pull down screen.  There are four network jacks."
    )
    third.rooms.create(
        name="3602",
        capacity=40,
        description="Used for formal and informal meetings with groups of 40 or less and is equipped with tables, chairs, and pull down screen.  There are 6 available network jacks.  Standard setup is auditorium style.\nDimensions: 25' 3\" X 36'\""
    )
    third.rooms.create(
        name="3606",
    	nickname="Shellnut Gallery",
        capacity=40,
        description="Used for formal and informal meetings with groups of 40 or less and is equipped with tables, chairs, and pull down screen.  There are 6 available network jacks."
    )
    second.rooms.create(
        name="2424",
        capacity=25,
        description="Used for formal and informal meetings with groups of 25 or less and is equipped with tables and chairs.  This room also features a private bathroom and lounge furniture, ideal for catering.  There are 6 available network jacks and TV hookup."
    )
    second.rooms.create(
        name="McNeil Room",
        capacity=500,
        description="Used for formal meetings, concerts, and large events with groups of 250 or less with chairs and tables, groups of 300 with chairs only, or groups of 500 standing only.  Staging, lighting, and media equipment is available.  This room is ideal for catering large events."
    )
    second.rooms.create(
        name="West Lobby",
        capacity=20,
        description=""
    )
    second.rooms.create(
        name="Welcome Lobby",
        capacity=20,
        description=""
    )
    first.rooms.create(
        name="Mother's",
        capacity=125,
        description="Used for informal meetings, concerts, and large events with groups of 125 or less.  The room is equipped with chairs, tables, piano, stage, and lighting.  There are 17 network jacks and TV hookup."
    )
