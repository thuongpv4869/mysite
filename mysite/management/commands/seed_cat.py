import datetime
from django.core.management.base import BaseCommand
from mysite.helpers import get_batch_index

from mysite.models import Cat


class Command(BaseCommand):
    help = 'seed cat data'

    def add_arguments(self, parser):
        parser.add_argument('--num', type=int, help="number of record",
                            default=100, metavar='n'
                            )
        parser.add_argument('--trun', help="truncate all",
                            action="store_true"
                            )

    def handle(self, *args, **options):
        if options['trun']:
            Cat.objects.all().delete()
            return

        CHUNK_SIZE = 2000
        start = datetime.datetime.now()
        print("start...")
        for list_index in get_batch_index(options['num'], CHUNK_SIZE):
            print(list_index[0])
            cats_batch = [Cat(name=f"cat {i}") for i in list_index]
            Cat.objects.bulk_create(cats_batch)

        print("success!")
        print(f"exc time: {datetime.datetime.now() - start}")
