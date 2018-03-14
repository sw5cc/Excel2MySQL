# -*- utf-8 -*-

import logging
import os
from .utils import get_files, insert_request


logger = logging.getLogger(__name__)


class Master(object):

    def __init__(self):
        self.state = ''

    def feed_dir(self, path):
        for file in get_files(path):
            self.feed_file(file)

    def feed_file(self, file):
        insert_request(file)
        print("Process file {0}".format(file))
