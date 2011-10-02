Setting up a Development Enviroment
===================================

These documents assume you are running on Ubuntu. If you aren't, ask us, and 
we'll come up with seperate instructions for your platform.

First, you'll need to install ``pip``, a Python installer::

    $ sudo apt-get install python-pip

This installs it via the system package manager.

Now we're going to use pip to install ``virtualenv`` and ``virtualenvwrappers``,
they're used to create isolated Python enviroments on your system. This is
useful if you have multiple projects (it lets you have multiple versions of the
same dependency), but also just to ensure you're always working with the right
packages::

    $ sudo pip install virtualenv virtualenvwrapper

``virtualenvwrapper`` has several bash scripts that you'll need to make sure
get loaded by your bash enviroment, to do this run::

    $ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

and restart your terminal.

Now you'll need to create an enviroment for the project, I called mine
``sdd-code``, you can name it whatever you like::

    $ mkvirtualenv sdd-code

This will create the environment, and will also activate it for your current
terminal session. When you create new terminal session to work on this, you'll 
need to re-activate it with::

    $ workon sdd-code

Finally you'll need to install the dependencies for this project with::

    $ pip install -r requirements.txt

And now you'll be able to run a local development server with::

    $ python rooms_project/manage.py runserver

Now just visit http://localhost:8000 in your browser. Enjoy!
