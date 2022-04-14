from django.core.management.base import BaseCommand
from apps.tourism.models import Users


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Users.objects.count() == 0:
            username = 'root'
            email = 'root@gmail.com'
            password = 'admin'
            print('Creating account for %s (%s)' % (username, email))
            admin = Users.objects.create_superuser(
                email=email, username=username, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
