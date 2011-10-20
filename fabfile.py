from fabric.api import local
from fabric.context_managers import lcd


def deploy():
    local("python rooms_project/manage.py collectstatic --noinput")
    with lcd("docs"):
        local("make html")
    local("epio upload")
    local("epio django syncdb")

def update_fixture_data():
    # TODO: verify there's no modified files
    local("python rooms_project/manage.py generate_fixture rooms.rpi_union --indent=4 > rooms_project/rooms/fixtures/rpi_union.json")
    local('git commit -a -m "Updated fixture data"')
    local("git push")
    local("epio django loaddata rooms_project/rooms/fixtures/rpi_union.json")
