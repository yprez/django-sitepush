from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand

from fabric.api import local

from optparse import make_option


class Command(BaseCommand):
    help = "Redeploy the current instance"

    option_list = BaseCommand.option_list + (
        make_option('--servername', action='store', type='string',
                    dest='servername', default='staging',
                    help='Server name - to pick which configuration to use'),
        make_option('--noreqs', action='store_true', dest='noreqs',
                    default=False, help='Don\'t update requirements'),
    )

    def handle(self, *args, **options):
        server_name = options.get('servername')

        noreqs = options.get('noreqs')

        if not server_name in settings.DEPLOYS:
            self.stderr.write('Non existant server config')
            return

        server = settings.DEPLOYS[server_name]

        local('git pull origin {0}'.format(server['BRANCH']))

        if not noreqs:
            local('pip install -r requirements.txt')

        management.call_command('syncdb',
                interactive=False, stdout=self.stdout)
        management.call_command('migrate',
                interactive=False, stdout=self.stdout)
        management.call_command('collectstatic',
                interactive=False, stdout=self.stdout)

        # Reload the app in the webserver
        ws = server['WEBSERVER']
        if ws == 'apache':
            local('touch {0}'.format(server['WSGI_FILE']))  # reload wsgi
        elif ws == 'gunicorn':
            local('sudo kill -HUP `cat {0}`'.format(server['PID_FILE']))
        else:
            self.stderr.write('Unknown webserver type!')
