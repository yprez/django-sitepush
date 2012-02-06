===============
django-sitepush
===============

Redeploy Django projects using management commands


What does it do?
----------------

Using Fabric to run a management command on each remote instance to redeploy
itself.

The remote command will pull the source code from Git, run all necessary Django
management commands, and restart the server.


Why not just write a Fabric script?
-----------------------------------

It's faster. When the you run everything remotely it only takes about 10
seconds to deploy an instance.


What commands will run?
-----------------------

- ``git pull``
- ``pip install -r requirements.txt``
- ``syncdb``
- ``migrate``
- ``collectstatic``
- ``restart server (webserver dependent)``



Requirements
============

- A deployed instance running either:
    - Apache with mod_WSGI
    - GUnicorn
- Fabric
- A virtualenv dedicated to the project.
- A Git hosted repository for the project



Installation
============

Add the app to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        #...
        'sitepush',
    )


Settings
========

Add the server configuration to your settings file::

    DEPLOYS = {
        'default': {
            'HOST': '192.168.0.1',         # IP or domain name
            'USER': 'user',                # User to login with
            'BRANCH': 'master',            # Git branch to pull updates from
            'SETTINGS': 'settings',        # Settings file to use (optional)
            'DIR': '/var/www/myproject/',
            'ENV': 'myvirtualenv',         # virtualenv used in the project
            'WEBSERVER': 'gunicorn',       # webserver - 'apache' or 'gunicorn'

            'PID_FILE': '/tmp/gunicorn.pid',  # Gunicorn pid file path
            'WSGI_FILE': 'deploy/wsgi.py',    # Apache wsgi file path
        },
    }

The ``PID_FILE`` / ``WSGI_FILE`` settings should be set depending on the web
server you're using.

``BRANCH`` is optional and defaults to ``master``


Usage
=====

::

    python manage.py deploy_remote default

    # Or
    python manage.py deploy_remote srv1 srv2 #...'

    # Don't install requirements:
    python manage.py deploy_remote default --noreqs

    # Deploy all remote instances:
    python manage.py deploy_remote --all
