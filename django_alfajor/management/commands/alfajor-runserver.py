from django.core.management.commands.testserver import Command as TestServerCommand
from optparse import make_option
import os
import sys
from django.conf import settings

class Command(TestServerCommand):

    def set_test_environment(self):
        try:
            test_db_name = 'test_' + settings.DATABASES['default']['NAME']
            if settings.DATABASES['default']['TEST_NAME']:
                test_db_name = settings.DATABASES['default']['TEST_NAME']
            settings.DATABASES['default']['NAME'] = test_db_name
        except AttributeError, ae:
            if settings.TEST_DATABASE_NAME:
                settings.DATABASE_NAME = settings.TEST_DATABASE_NAME
            else:
                settings.DATABASE_NAME = 'test_' + settings.DATABASE_NAME

    def handle(self, *fixture_labels, **options):
        from django.core.management import call_command
        self.set_test_environment()

        verbosity = int(options.get('verbosity', 1))
        addrport = options.get('addrport')

        shutdown_message = '\nServer stopped.'
        call_command('runserver', addrport=addrport, shutdown_message=shutdown_message, use_reloader=False)
