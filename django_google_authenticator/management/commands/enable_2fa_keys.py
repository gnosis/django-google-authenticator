from subprocess import check_call, CalledProcessError
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django_google_authenticator.models import Google
from django.conf import settings
import pyotp


class Command(BaseCommand):
    help = 'Generates Google Auth keys and enables 2FA'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--username',
            default=None,
            help='Enable 2FA for a certain admin user',
        )

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.SUCCESS('Starting enabling Google Auth keys'))
            users = None
            # If username is not None, we passed a value via parameters
            if options.get('username'):
                users = User.objects.filter(is_superuser=True, username=options.get('username'))
            else:
                users = User.objects.filter(is_superuser=True)

            for user in users:
                if not hasattr(user, 'google'):
                    # create google key for that user
                    self.stdout.write(self.style.SUCCESS('Creating auth key for user {}'.format(user.username)))
                    google = Google()
                    google.user = user
                    google.gauth_key = pyotp.random_base32()
                    google.save()
                    self.stdout.write(self.style.SUCCESS('Auth key for user {} created: KEY: {}'.format(user.username, google.gauth_key)))
                else:
                    self.stdout.write(self.style.WARNING('2FA already active for user {}'.format(user.username)))
            self.stdout.write(self.style.SUCCESS('Google Auth creation process ended successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Google Auth error: {}'.format(e.message)))
