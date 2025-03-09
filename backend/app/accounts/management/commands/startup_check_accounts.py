from django.core.management.base import BaseCommand

from accounts.managers import StartUpManager


class Command(BaseCommand):
    help = "Checks before starting for bash script."
    requires_migrations_checks = True

    def handle(self, *args, **options):
        StartUpManager.startup_actions()
