from fabric.api import local
from fabric.context_managers import lcd


def deploy():
    local("python rooms_project/manage.py collectstatic --noinput")
    with lcd("docs"):
        local("make html")
    local("epio upload")
    local("epio django syncdb")
