# from abc import abstractclassmethod
from typing import overload
import pymongo
import random
from .__init__ import *
# import uuid

class Collect(object):                   # Abstract class
    def __init__(self, col_name) -> None:
        self.col = db[col_name]

class Plans(Collect):
    def __init__(self, col_name='plans') -> None:
        super().__init__(col_name)
    def add_plan(self, time: str, op, data=12):
        uuid1 = time.replace(':', '') + ''.join(random.choices(list('0123456789abcdef'), k=4)) + '-'
        uuid2 = ''.join(random.choices(list('0123456789abcdef'), k=4)) + '-'
        uuid3 = ''.join(random.choices(list('0123456789abcdef'), k=4)) + '-'
        uuid4 = ''.join(random.choices(list('0123456789abcdef'), k=16))
        uuid = uuid1 + uuid2 + uuid3 + uuid4
        data = [{'time' : time, 'op' : op, 'uuid' : uuid, 'data' : data}]
        self.col.insert_many(data)
    def delete_plan(self, uuid):
        query = {'uuid' : uuid}
        self.col.delete_one(query)
    def update_plan(self, uuid, time, op, data=12):
        query = {'uuid' : uuid}
        new = {'$set' : {'time' : time, 'op' : op, 'data' : data}}
        self.col.update_one(query, new)
    def get_all_plans(self):
        return self.col.find()

class Waiting(Collect):
    def __init__(self, col_name='waiting') -> None:
        super().__init__(col_name)
    def add_waiting(self, op, data):
        data = [{'op' : op, 'data' : data}]
        self.col.insert_many(data)
    def get_waiting(self):
        return self.col.find_one_and_delete({'op' : {'$ne' : -2147483648}})

# class 

# if __name__ == '__main__': 
#     # waiting = Waiting()
#     plans = Plans()
#     plans.delete_plan('01a5bd72-6e18-11ec-a800-dca632c36146')
#     plans.add_plan('19:30', 0, 12)
