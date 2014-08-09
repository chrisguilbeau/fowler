import logging
import datetime

logging.basicConfig(
    filename='../logs/{}.log'.format(datetime.datetime.now()))
warn = logging.warning
log = logging.info

