# -*- utf-8 -*-

from Excel2MySQL import Master

def run_master():
    master = Master()
    master.feed_dir('E:/sw5cc/test/data/xlsx')


if __name__ == '__main__':
    run_master()