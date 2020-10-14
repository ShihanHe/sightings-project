import csv
import re

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Import the csv to database'

    def add_arguments(self,parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kargs):



