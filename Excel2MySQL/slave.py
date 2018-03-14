# -*- utf-8 -*-

from time import sleep
from .utils import pop_request, bytes_to_str
from .dumps import xls2db


class Slave(object):

    def next_requests(self):
        return pop_request()

    def start_requests(self):
        return self.next_requests()

    def process(self):
        while True:
            req = self.next_requests()
            if req:
                file = bytes_to_str(req)
                print("xls2db: {0}".format(file))
                xls2db(file)
            else:
                print("Empty queue, waiting...")
                sleep(1)


