from django.core.management.base import BaseCommand
from invitations.models import Invitation

class Command(BaseCommand):
    def handle(self, *args, **options):
        Invitation.objects.delete_expired_confirmations()
