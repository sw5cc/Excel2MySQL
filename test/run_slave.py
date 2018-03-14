# -*- utf-8 -*-

from Excel2MySQL import Slave


def run_slave():
    slave = Slave()
    slave.process()


if __name__ == '__main__':
    run_slave()