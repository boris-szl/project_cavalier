from django.core.management.base import BaseCommand
from app1.models import RoicData

import sys
import os

sys.path.insert(0, "/Users/boris.szelcsanyi/Programming/projects/metrixx/venv/src/app1/modules")
import findata
import company
from sqlalchemy import create_engine

class Command(BaseCommand):
	help = "A command to add data from YFinance to the database"
	# user = base.DATABASE['default']['USER']
	# password = base.DATBASE['default']['PASSWORD']
	# database_name = base.DATBASE['defualt']['NAME']

	def handle(self, *args, **options):
		# method of the class Command
		# this handle is called
		ticker = "V"
		# target referenziert auf das Objekt Company
		target = company.Company(ticker)
		df = target.getRoicTable()
		database_url = 'postgresql+psycopg2://{user}:{password}@localhost/{database_name}'.format(user="boris.szelcsanyi", password="jqee55jqee55", database_name="metrixx")
		engine = create_engine(database_url, echo=False)
		df.to_sql(RoicData._meta.db_table, if_exists='replace', con=engine, index=True)