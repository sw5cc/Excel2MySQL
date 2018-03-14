# -*- utf-8 -*-

import os
import redis as redis
import logging
from settings import *


logger = logging.getLogger(__name__)


def get_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(tuple(EXCEL_EXT)):
                # yield os.path.join(root, file)
                yield root + '/' + file


def insert_request(arg):
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_REQUEST_DB)
    except:
        logger.error("connect redis failed")
    else:
        r.lpush('slave:requests', arg)
        print("Insert {0} to redis".format(arg))


def pop_request():
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_REQUEST_DB)
    except:
        logger.error("connect redis failed")
    else:
        return r.lpop('slave:requests')


def bytes_to_str(s, encoding='utf-8'):
    if isinstance(s, bytes):
        return s.decode(encoding)
    return s