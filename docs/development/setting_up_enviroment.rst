Setting up a Development Enviroment
===================================

These documents assume you are running on Ubuntu, if you aren't ask us, we'll
come up with seperate instructions for your platform.

First, you'll need to install ``pip``, a Python installer::

    $ sudo apt-get install python-pip

This installs it via the system package manager.

Now we're going to use pip to install ``virtualenv`` and ``virtualenvwrappers``,
they're used to create isolated Python enviroments on your system. This is
useful if you have multiple projects (it lets you have multiple versions of the
same dependency), but also just to ensure you're always working with the right
packages.

    $ sudo pip install virtualenv virtualenvwrapper

Now you'll need to create an enviroment for the project, I called mine
``sdd-code``, you can name it whatever you like:

    $ mkvirtualenv sdd-code

This will create the environment, and also activate it for your current
terminal, when you create new terminal session to work on this, you'll need to
re-activate it with::

    $ workon sdd-code

Finally you'll need to install the dependencies for this project with::

    $ pip install -r requirements.txt

And now you'll be able to run a local development server with::

    $ python rooms_project/manage.py runserver

And if you visit http://localhost:8000 in your browser, it'll have the
site up.