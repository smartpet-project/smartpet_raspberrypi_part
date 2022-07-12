import sys
sys.path = sys.path + ['/home/pi/smartpet/']
from ..__init__ import *

class Transfer(Collect):
    def __init__(self, col_name='transfer') -> None:
        super().__init__(col_name)
    def send_detect_signal(self) -> None:
        data = {'owner': 2, 'op': 1, 'data': 180}
        self.col.insert_one(data)
    def get_detect_result(self) -> bool:
        query = {'owner': 2, 'op': 2}
        result = self.col.find_one_and_delete(query)
        return True if result == '1' else False
    def feed(self, data):
        # arduino.open()
        # arduino.write(b'f' + str(data).encode('utf8'))
        # arduino.close()
        print('simulation feed.')

if __name__ == '__main__': 
    test = Transfer()
    test.feed(12)
