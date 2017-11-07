from subprocess import check_call, CalledProcessError
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from DjangoGoogleAuthenticator.models import Google
from django.conf import settings
import pyotp


class Command(BaseCommand):
    help = 'Generates Google Auth keys and enables 2FA'

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.SUCCESS('Starting creating Google Auth keys'))
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
            self.stdout.write(self.style.SUCCESS('Google Auth creation process ended successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Google Auth error: {}'.format(e.message)))
