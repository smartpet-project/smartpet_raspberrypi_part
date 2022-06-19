# from smartpet.database.databases import Waiting
from . import *

def start_query_daemon():
    waits = waiting.get_waiting()
    
