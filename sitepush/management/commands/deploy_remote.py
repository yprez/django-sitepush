from django.conf import settings
from django.core.management.base import BaseCommand

from fabric.api import run, cd, env, prefix

from optparse import make_option
import time


class Command(BaseCommand):
    help = """Redeploy the application on a remote server"""
    args = "<server_name server_name ...>"

    option_list = BaseCommand.option_list + (
        make_option('--noreqs', action='store_true', dest='reqs',
                    default=False, help='Update requirements'),
        make_option('--all', action='store_true', dest='all',
                    default=False, help='Update all instances'),
    )

    def handle(self, *args, **options):
        noreqs = options.get('reqs')
        all = options.get('all')

        if not args and not all:
            self.stderr.write('No servers selected\n')
            return

        if all:
            servers = settings.DEPLOYS
        else:
            servers = dict([(k, v) for k, v in settings.DEPLOYS.items()
                                   if k in args])

        not_found = set(args) - set(servers.keys())

        for n in not_found:
            self.stderr.write('Error - server {0} not found\n'.format(n))

        for name, server in servers.items():
            self.deploy(server, name, noreqs)

    def deploy(self, server, server_name, noreqs=False):
        starttime = time.time()
        env.host_string = '{0}@{1}'.format(server['USER'], server['HOST'])
        self.stdout.write('Depoloying to "{0}"...\n'.format(server_name))

        cmd = ('python manage.py deploy_local --servername={servername} ' +
               '{noreqs} --settings={settings}'). \
               format(noreqs='--noreqs' if noreqs else '',
                      settings=server['SETTINGS'] if 'SETTINGS' in server
                                                  else 'settings',
                  servername=server_name)

        with cd(server['DIR']):
            run('git pull origin {0}'.format(server['BRANCH']))

            with prefix('workon {0}'.format(server['ENV'])):
                run(cmd)

        self.stdout.write('Deployed successfully\n')
        self.stdout.write('Time elapsed: {0} seconds\n\n'.\
                format(time.time() - starttime))
