===============
django-sitepush
===============

**Warning:** This package is still in alpha, and not really ready for use.


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

            'PID_FILE': '/tmp/gunicorn.pid',  # Gunicorn pid file location
            'WSGI_FILE': 'deploy/wsgi.py',    # Apache wsgi file location
        },
    }

The ``PID_FILE`` / ``WSGI_FILE`` settings should be set depending on the web
server you're using.

``BRANCH`` is optional and defaults to ``master``

