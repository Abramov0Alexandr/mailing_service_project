from django.core.management import BaseCommand
from custom_user.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = CustomUser.objects.create(
            email='admin@project.org',
            fullname='alexa',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password('661104')
        user.save()
