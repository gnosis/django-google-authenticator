from subprocess import check_call, CalledProcessError
from django.core.management.base import BaseCommand
from django_google_authenticator.models import Google
from django.conf import settings
import pyotp


class Command(BaseCommand):
    help = 'Disable 2FA keys'

    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument(
            '--username',
            default=None,
            help='Disable 2FA for a certain admin user',
        )

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.SUCCESS('Starting disabling Google Auth keys'))
            auths = None
            if options.get('username'):
                auths = Google.objects.filter(user__username=options.get('username'))
            else:
                auths = Google.objects.all()

            auths.delete()
            self.stdout.write(self.style.SUCCESS('Google Auth disabled successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Google Auth error: {}'.format(e.message)))
