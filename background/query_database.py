# from smartpet.database.databases import Waiting
from . import *

def start_query_database():
    waits = waiting.get_waiting()
    if waits != None:
        transfer.feed(waits['data'])
