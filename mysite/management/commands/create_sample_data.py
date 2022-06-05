from django.utils import timezone
from django.core.management.base import BaseCommand

from mysite.models.user import UserFullInfo


class Command(BaseCommand):
    help = 'create sample data'

    # def add_arguments(self, parser):
    #     parser.add_argument('--num', type=int, help="number of record",
    #                         default=100, metavar='n'
    #                         )
    #     parser.add_argument('--trun', help="truncate all",
    #                         action="store_true"
    #                         )

    def handle(self, *args, **options):

        start = timezone.now()
        print("start...")

        print("creating superuser...")
        superuser = UserFullInfo(
            email="admin@admin.com",
            first_name="super",
            last_name="user",
            date_of_birth=timezone.now(),
            is_superuser=True,
            is_active=True,
            is_admin=True,
        )
        superuser.set_password("admin")
        superuser.save()
        print("done create superuser")

        print("success!")
        print(f"exc time: {timezone.now() - start}")
