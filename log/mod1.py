import logging
import os
# create logger
logger = logging.getLogger('foo')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.FileHandler('example.log')
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('foo --- %(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger

logger.addHandler(ch)
filename = 'E:/experiment/log/change_file.log'
stream_open = open(filename, 'a')
print stream_open
handler_obj = logger.handlers[0]
# handler_obj.stream = stream_open
# handler_obj.__init__(filename)
print handler_obj.__dict__
# logger.handlers[0].baseFilename = 'E:/experiment/log/change_file.log'
logger.info('aaaaaaaaaaa')
